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
    #region Window
    public StencilCSG() : base(800, 600, new GraphicsMode(new ColorFormat(8, 8, 8, 8), 24, 8)) // request 8-bit stencil buffer
    {
        base.VSync = VSyncMode.Off;
        KeyDown += delegate(object sender, KeyboardKeyEventArgs e)
        {
            switch (e.Key)
            {
                case Key.Escape: this.Exit(); break;
                case Key.Space: ShowDebugWireFrame = !ShowDebugWireFrame; break;
            }
        };
    }

    protected override void OnResize(EventArgs e)
    {
        GL.Viewport(0, 0, Width, Height);
        GL.MatrixMode(MatrixMode.Projection);
        Matrix4 p = Matrix4.CreatePerspectiveFieldOfView(MathHelper.PiOver4, Width / (float)Height, 0.1f, 64.0f);
        GL.LoadMatrix(ref p);
    }
    #endregion Window

    protected override void OnLoad(EventArgs e)
    {
        #region Abort on platforms which will not be able to execute the ops properly
        #endregion Abort on platforms which will not be able to execute the ops properly
        WindowTitle = "Cube-Sphere Stencil CSG  " + GL.GetString(StringName.Renderer) + " (GL " + GL.GetString(StringName.Version) + ")";

        #region GL States
        GL.ClearColor(.08f, .12f, .16f, 1f);

        GL.Enable(EnableCap.DepthTest);
        GL.DepthFunc(DepthFunction.Less);
        GL.ClearDepth(1.0);

        GL.Enable(EnableCap.StencilTest);
        GL.ClearStencil(0);
        GL.StencilMask(0xFFFFFFFF); // read&write

        GL.Enable(EnableCap.CullFace);
        GL.FrontFace(FrontFaceDirection.Ccw);
        GL.CullFace(CullFaceMode.Back);

        GL.PolygonMode(MaterialFace.FrontAndBack, PolygonMode.Fill);

        GL.Color4(1f, 1f, 1f, 1f);

        GL.Enable(EnableCap.Lighting);
        GL.Enable(EnableCap.Light0);
        GL.ShadeModel(ShadingModel.Smooth);
        #endregion GL States

        #region Load Texture
        Bitmap bitmap = new Bitmap("Data/Textures/logo-dark.jpg");
        bitmap.RotateFlip(RotateFlipType.RotateNoneFlipY);

        GL.GenTextures(1, out Texture);
        GL.BindTexture(TextureTarget.Texture2D, Texture);

        BitmapData data = bitmap.LockBits(new System.Drawing.Rectangle(0, 0, bitmap.Width, bitmap.Height), ImageLockMode.ReadOnly, System.Drawing.Imaging.PixelFormat.Format32bppArgb);
        GL.TexImage2D(TextureTarget.Texture2D, 0, PixelInternalFormat.Rgba, data.Width, data.Height, 0, OpenTK.Graphics.OpenGL.PixelFormat.Bgra, PixelType.UnsignedByte, data.Scan0);
        GL.TexParameter(TextureTarget.Texture2D, TextureParameterName.TextureMinFilter, (int)TextureMinFilter.Linear);
        GL.TexParameter(TextureTarget.Texture2D, TextureParameterName.TextureMagFilter, (int)TextureMagFilter.Linear);
        GL.Finish();
        bitmap.UnlockBits(data);
        #endregion Load Texture

        OperandA = new ChamferCube(1.5, 2.0, 2.5, ChamferCube.SubDivs.Four, 0.42, true);
        OperandB = new SlicedSphere(2.0f, Vector3d.Zero,
                                       SlicedSphere.eSubdivisions.Three,
                                       new SlicedSphere.eDir[] { SlicedSphere.eDir.All },
                                       true);

        #region Invert Operand B's Normals
        // only the inside of the operand is ever drawn to color buffers and lighting requires this.
        PrimitiveType tempPrimMode;
        VertexT2dN3dV3d[] tempVertices;
        uint[] tempIndices;

        OperandB.GetArraysforVBO(out tempPrimMode, out tempVertices, out tempIndices);
        OperandB.Dispose();

        for (int i = 0; i < tempVertices.Length; i++)
        {
            tempVertices[i].Normal *= -1.0;
            tempVertices[i].Normal.Normalize();
        }

        OperandB = new VboShape(ref tempPrimMode, ref tempVertices, ref tempIndices, true);
        #endregion Invert Operand B's Normals
    }

    protected override void OnUnload(EventArgs e)
    {
        GL.DeleteTextures(1, ref Texture);
        OperandA.Dispose();
        OperandB.Dispose();
        base.OnUnload(e);
    }

    }
}
