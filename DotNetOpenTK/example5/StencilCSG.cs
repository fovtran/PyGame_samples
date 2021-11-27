using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Diagnostics;

using OpenTK;
using OpenTK.Input;
using OpenTK.Graphics;
using OpenTK.Graphics.OpenGL;

using Examples.Shapes;

namespace Examples.Tutorial
{
    partial class StencilCSG : GameWindow
    {
        #region Model Related
        DrawableShape OperandB;
        DrawableShape OperandA;
        float MySphereZOffset = 5f;
        float MySphereXOffset = 0f;
        int Texture;
        #endregion Model Related

        string WindowTitle;
        bool ShowDebugWireFrame = true;

        float CameraZoom;
        float CameraRotX;
        float CameraRotY;
        Vector3 EyePosition = new Vector3(0f, 0f, 15f);

        protected override void OnUpdateFrame(FrameEventArgs e)
        {
            var mouse = OpenTK.Input.Mouse.GetState();
            CameraRotX = -mouse.X * .5f;
            CameraRotY = mouse.Y * .5f;
            CameraZoom = mouse.Wheel * .2f;
        }

        public void DrawOperandB()
        {
            GL.PushMatrix();
            GL.Translate(Math.Cos(MySphereXOffset), -1f, Math.Cos(MySphereZOffset));
            OperandB.Draw();
            GL.PopMatrix();
        }

        public void DrawOperandA()
        {
            GL.Enable(EnableCap.Texture2D);
            OperandA.Draw();
            GL.Disable(EnableCap.Texture2D);
        }

        public void RenderCsg()
        {
            // first pass
            GL.Disable(EnableCap.StencilTest);

            GL.ColorMask(false, false, false, false);
            GL.CullFace(CullFaceMode.Front);
            DrawOperandB();// draw front-faces into depth buffer

            // use stencil plane to find parts of b in a
            GL.DepthMask(false);
            GL.Enable(EnableCap.StencilTest);
            GL.StencilFunc(StencilFunction.Always, 0, 0);

            GL.StencilOp(StencilOp.Keep, StencilOp.Keep, StencilOp.Incr);
            GL.CullFace(CullFaceMode.Back);
            DrawOperandA(); // increment the stencil where the front face of a is drawn

            GL.StencilOp(StencilOp.Keep, StencilOp.Keep, StencilOp.Decr);
            GL.CullFace(CullFaceMode.Front);
            DrawOperandA(); // decrement the stencil buffer where the back face of a is drawn

            GL.DepthMask(true);
            GL.Disable(EnableCap.DepthTest);

            GL.ColorMask(true, true, true, true);
            GL.StencilFunc(StencilFunction.Notequal, 0, 1);
            DrawOperandB(); // draw the part of b that's in a

            // fix depth
            GL.ColorMask(false, false, false, false);
            GL.Enable(EnableCap.DepthTest);
            GL.Disable(EnableCap.StencilTest);
            GL.DepthFunc(DepthFunction.Always);
            DrawOperandA();
            GL.DepthFunc(DepthFunction.Less);

            // second pass
            GL.CullFace(CullFaceMode.Back);
            DrawOperandA();

            GL.DepthMask(false);
            GL.Enable(EnableCap.StencilTest);

            GL.StencilFunc(StencilFunction.Always, 0, 0);
            GL.StencilOp(StencilOp.Keep, StencilOp.Keep, StencilOp.Incr);
            DrawOperandB(); // increment the stencil where the front face of b is drawn

            GL.StencilOp(StencilOp.Keep, StencilOp.Keep, StencilOp.Decr);
            GL.CullFace(CullFaceMode.Front);
            DrawOperandB(); // decrement the stencil buffer where the back face of b is drawn

            GL.DepthMask(true);
            GL.Disable(EnableCap.DepthTest);

            GL.ColorMask(true, true, true, true);
            GL.StencilFunc(StencilFunction.Equal, 0, 1);
            GL.CullFace(CullFaceMode.Back);
            DrawOperandA(); // draw the part of a that's in b

            GL.Enable(EnableCap.DepthTest);
        }

        protected override void OnRenderFrame(FrameEventArgs e)
        {
            this.Title = WindowTitle + "  FPS: " + (1f / e.Time).ToString("0.");

            MySphereZOffset += (float)(e.Time * 3.1);
            MySphereXOffset += (float)(e.Time * 4.2);

            #region Transform setup
            GL.Clear(ClearBufferMask.ColorBufferBit | ClearBufferMask.DepthBufferBit | ClearBufferMask.StencilBufferBit);

            // Camera
            GL.MatrixMode(MatrixMode.Modelview);
            Matrix4 mv = Matrix4.LookAt(EyePosition, Vector3.Zero, Vector3.UnitY);
            GL.LoadMatrix(ref mv);

            GL.Translate(0f, 0f, CameraZoom);
            GL.Rotate(CameraRotX, Vector3.UnitY);
            GL.Rotate(CameraRotY, Vector3.UnitX);
            #endregion Transform setup

            RenderCsg();

            if (ShowDebugWireFrame)
            {
                GL.Color3(System.Drawing.Color.LightGray);
                GL.Disable(EnableCap.StencilTest);
                GL.Disable(EnableCap.Lighting);
                //GL.Disable( EnableCap.DepthTest );
                GL.PolygonMode(MaterialFace.Front, PolygonMode.Line);
                DrawOperandB();
                GL.PolygonMode(MaterialFace.Front, PolygonMode.Fill);
                GL.Enable(EnableCap.DepthTest);
                GL.Enable(EnableCap.Lighting);
                GL.Enable(EnableCap.StencilTest);
            }
            this.SwapBuffers();
        }

        [STAThread]
        static void Main()
        { using (StencilCSG example = new StencilCSG()) { example.Run(30.0, 0.0); } }
    }
}
