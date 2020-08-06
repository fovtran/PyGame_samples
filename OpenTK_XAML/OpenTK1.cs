using OpenTK;
using OpenTK.Graphics.OpenGL;
using System;
using System.Drawing;
using System.Windows;
using System.Windows.Threading;

namespace OpenTkControl {
  public partial class MainWindow : Window {

    private DispatcherTimer _Timer;
    private DateTime _ProgramStartTime;

    public MainWindow() {
      InitializeComponent();

      _ProgramStartTime = DateTime.Now;

      _Timer = new DispatcherTimer(DispatcherPriority.Send);
      _Timer.IsEnabled = true;
      _Timer.Interval = new TimeSpan(0, 0, 0, 0, 30);
      _Timer.Tick += OnTimer;
      _Timer.Start();
    } // constructor

    void OnTimer(object sender, EventArgs e) {
      OpenTkControl.Invalidate();
    } //

    private void OpenTkControl_Paint(object sender, System.Windows.Forms.PaintEventArgs e) {
      GLControl lControl = OpenTkControl;

      // Reset the depth and color buffer.
      // We want to render a new world. We do not want to continue with a previous rendering.
      GL.Clear(ClearBufferMask.ColorBufferBit | ClearBufferMask.DepthBufferBit);

      // Create a projection matrix transforming camera space to raster space. (google for "view frustum")
      // Which is like: Press the 3D world and make it flat like a pancake, so that it does fit on the 2D screen.
      //                All points between a distance of 1 and 1000 will be taken into account.
      float lAngleView = 1.2f;              // y direction (in radians)
      float lAspectRatio = 4f / 3f;         // width / height
      float lDistanceToNearClipPlane = 1f;
      float lDistanceToFarClipPlane = 1000f;
      Matrix4 lPerspective = Matrix4.CreatePerspectiveFieldOfView(lAngleView, lAspectRatio, lDistanceToNearClipPlane, lDistanceToFarClipPlane);
      GL.MatrixMode(MatrixMode.Projection); GL.LoadIdentity(); GL.LoadMatrix(ref lPerspective);

      // camera setup
      Vector3 lCameraLocation = new Vector3(100f, 10f, 0f);
      Vector3 lCameraLookingAt = new Vector3(0f, 0f, 0f);     // look at the center of the coordinate system
      Vector3 lCameraWhatIsUpside = new Vector3(0f, 1f, 0f);  // classical way to hold a camera
      Matrix4 lCamera = Matrix4.LookAt(lCameraLocation, lCameraLookingAt, lCameraWhatIsUpside);
      GL.MatrixMode(MatrixMode.Modelview); GL.LoadIdentity(); GL.LoadMatrix(ref lCamera);

      // this is the size on the screen
      GL.Viewport(0, 0, lControl.Width, lControl.Height);

      // only draw the nearest pixels and not pixels that are actually hidden by other pixels
      GL.Enable(EnableCap.DepthTest);
      GL.DepthFunc(DepthFunction.Less);

      // set time dependent variables to generate movements
      double lTotalMillis = DateTime.Now.Subtract(_ProgramStartTime).TotalMilliseconds;
      double lTime1 = (lTotalMillis % 10000.0) / 10000.0; // between 0 and 1
      double lTime2 = (lTotalMillis % 2000.0) / 2000.0;   // between 0 and 1
      double lTimeRadians = lTime2 * 2.0 * Math.PI;
      float lJump = (float)(-20.0 + 10.0 * Math.Sin(lTimeRadians));
      float lRadius = -40f;

      // add the comet
      DrawComet(lTotalMillis);

      // render the floor
      GL.Rotate(360.0 * lTime1, 0.0, 1.0, 0.5);  // rotate around y axis and half as much around z axis
      DrawFloor();

      // render objects
      // from where we are; now rotate the objects into the opposite direction
      GL.Rotate(-lTime1 * 360.0 * 2.0, 0.0, 1.0, 0.0); DrawAvatar("Merlin", -30f, lRadius);
      GL.Rotate(60.0, 0.0, 1.0, 0.0); DrawAvatar("Freya", lJump, lRadius);
      GL.Rotate(60.0, 0.0, 1.0, 0.0); DrawAvatar("Steve", -30f, lRadius);
      GL.Rotate(60.0, 0.0, 1.0, 0.0); DrawAvatar("Merlin", lJump, lRadius);
      GL.Rotate(60.0, 0.0, 1.0, 0.0); DrawAvatar("Freya", -30f, lRadius);
      GL.Rotate(60.0, 0.0, 1.0, 0.0); DrawAvatar("Steve", lJump, lRadius);

      // render the cube in the center
      //GL.Rotate(360f * lTime2, 0f, 0f, 0f); // <= this kind of rotation lets the box bounce and change its size
      DrawCube(Color.SteelBlue, Color.DarkBlue, 0f, -25f, 0f, 8f, false);

      OpenTK.Graphics.GraphicsContext.CurrentContext.VSync = true; // caps GPU frame rate
      lControl.SwapBuffers();  // display our newly generated buffer with all objects
    } //

    private void DrawAvatar(string xName, float yShift, float zShift) {
      Icon lIcon = new Icon("Resources/" + xName + ".ico");
      Bitmap lBitmap = lIcon.ToBitmap();
      int lWidth = lBitmap.Width; float lHalfWidth = lWidth / 2f;
      int lHeight = lBitmap.Height; float lHalfHeight = lHeight;
      for (int y = 0; y < lHeight; y++) {
        for (int x = 0; x < lWidth; x++) {
          Color lColor = lBitmap.GetPixel(x, y);
          if (lColor.A != 0) DrawCube(lColor, lColor, (float)x - lHalfWidth, lHeight + yShift - (float)y, (float)zShift, 1f, true);
        }
      }
    } //

    private void DrawFloor() {
      for (int x = -100; x < 100; x += 10) {
        for (int z = -100 + (x % 10 == 0 ? 5 : 0); z < 100; z += 10) {
          DrawCube(Color.White, Color.Gray, x, -30f, z, 5f, false);
        }
      }
    } //

    private void DrawComet(double xTotalMillis) {
      xTotalMillis = (xTotalMillis % 7000.0) / 7000.0; // between 0 and 1

      GL.PushMatrix();
      GL.LoadIdentity();
      GL.Translate(xTotalMillis * 30f - 40f , 40f,  400f * xTotalMillis - 400f);
      GL.Rotate(360f * xTotalMillis * 3f, 1f, 1f, 1f);
      DrawTetrahedron(Color.Orange, Color.OrangeRed, 0f, 0f, 0f, 8f);
      GL.Rotate(180f, 1f, 0f, 0f);
      DrawTetrahedron(Color.Orange, Color.OrangeRed, 0f, 0f, 0f, 8f);
      GL.PopMatrix();
    } //

    private void DrawCube(System.Drawing.Color xColor, System.Drawing.Color xColor2, float X, float Y, float Z, float xWidth, bool xHasDarkBack) {
      float lHalfWidth = xWidth / 2f;
      float lTop = Y + lHalfWidth;
      float lBottom = Y - lHalfWidth;
      float lLeft = X - lHalfWidth;
      float lRight = X + lHalfWidth;
      float lFront = Z + lHalfWidth;
      float lRear = Z - lHalfWidth;

      GL.Begin(PrimitiveType.Quads);

      Color lColor; if (xHasDarkBack) lColor = Color.DarkGray; else lColor = xColor;
      Color lColor2; if (xHasDarkBack) lColor2 = Color.DarkGray; else lColor2 = xColor2;

      Action lPointFrontTopLeft = () => { GL.Color3(xColor); GL.Vertex3(lLeft, lTop, lFront); };
      Action lPointFrontTopRight = () => { GL.Color3(xColor2); GL.Vertex3(lRight, lTop, lFront); };
      Action lPointFrontBottomLeft = () => { GL.Color3(xColor2); GL.Vertex3(lLeft, lBottom, lFront); };
      Action lPointFrontBottomRight = () => { GL.Color3(xColor2); GL.Vertex3(lRight, lBottom, lFront); };
      Action lPointRearTopLeft = () => { GL.Color3(lColor); GL.Vertex3(lLeft, lTop, lRear); };
      Action lPointRearTopRight = () => { GL.Color3(lColor2); GL.Vertex3(lRight, lTop, lRear); };
      Action lPointRearBottomLeft = () => { GL.Color3(lColor2); GL.Vertex3(lLeft, lBottom, lRear); };
      Action lPointRearBottomRight = () => { GL.Color3(lColor2); GL.Vertex3(lRight, lBottom, lRear); };

      // front square
      lPointFrontTopLeft(); lPointFrontTopRight(); lPointFrontBottomRight(); lPointFrontBottomLeft();

      // rear square
      lPointRearTopLeft(); lPointRearTopRight(); lPointRearBottomRight(); lPointRearBottomLeft();

      // top square
      lPointFrontTopLeft(); lPointFrontTopRight(); lPointRearTopRight(); lPointRearTopLeft();

      // bottom square
      lPointFrontBottomLeft(); lPointFrontBottomRight(); lPointRearBottomRight(); lPointRearBottomLeft();

      // left square
      lPointFrontTopLeft(); lPointRearTopLeft(); lPointRearBottomLeft(); lPointFrontBottomLeft();

      // right square
      lPointFrontTopRight(); lPointRearTopRight(); lPointRearBottomRight(); lPointFrontBottomRight();

      GL.End();
    } //

    private void DrawTetrahedron(System.Drawing.Color xColor, System.Drawing.Color xColor2, float X, float Y, float Z, float xSideLength) {
      float lDistMidToVertex = (float)Math.Sqrt(6.0) / 4f * xSideLength;
      float lDistMidToFloor = (float)Math.Sqrt(6.0) / 12f * xSideLength;
      float lHeight = (float)Math.Sqrt(2.0 / 3.0) * xSideLength; // = lDistMidToVertex + lDistMidToEdge
      float lTop = Y + lDistMidToVertex;
      float lBottom = Y - lDistMidToFloor;
      float lRight = X + xSideLength / 2f;
      float lLeft = X - xSideLength / 2f;
      float lRear = Z - (float) (xSideLength * Math.Sqrt(3.0) / 3.0);
      float lFront = Z + (float)(xSideLength * Math.Sqrt(3.0) / 6.0);
 
      GL.Begin(PrimitiveType.Triangles);

      Action lPointTop = () => { GL.Color3(xColor); GL.Vertex3(X, lTop, Z); };
      Action lPointFrontBottomLeft = () => { GL.Color3(xColor2); GL.Vertex3(lLeft, lBottom, lFront); };
      Action lPointFrontBottomRight = () => { GL.Color3(xColor); GL.Vertex3(lRight, lBottom, lFront); };
      Action lPointRear = () => { GL.Color3(xColor2); GL.Vertex3(X, lBottom, lRear); };

      // front triangle
      lPointTop(); lPointFrontBottomLeft(); lPointFrontBottomRight();

      // left triangle
      lPointTop(); lPointFrontBottomLeft(); lPointRear();

      // right triangle
      lPointTop(); lPointFrontBottomRight(); lPointRear();

      // bottom triangle
      lPointFrontBottomLeft(); lPointFrontBottomRight(); lPointRear();

      GL.End();
    } //

  } // class
} // namespace
