using System;
using System.Drawing;
using OpenTK;
using OpenTK.Graphics.OpenGL;
using OpenTK.Input;

namespace Examples.Tutorial
{
    // [Example("GameWindow Simple", ExampleCategory.OpenTK, "GameWindow", 1, Documentation = "GameWindowSimple")]
    public class SimpleWindow : GameWindow
    {
        public SimpleWindow() : base(800, 600) { KeyDown += Keyboard_KeyDown; }

        #region Keyboard_KeyDown
        void Keyboard_KeyDown(object sender, KeyboardKeyEventArgs e)
        {
            if (e.Key == Key.Escape)
                this.Exit();

            if (e.Key == Key.F11)
                if (this.WindowState == WindowState.Fullscreen)
                    this.WindowState = WindowState.Normal;
                else
                    this.WindowState = WindowState.Fullscreen;
        }

        #endregion

        #region OnLoad
        protected override void OnLoad(EventArgs e) { GL.ClearColor(Color.MidnightBlue); }
        #endregion

        #region OnResize
        protected override void OnResize(EventArgs e)
        {
            GL.Viewport(0, 0, Width, Height);
            GL.MatrixMode(MatrixMode.Projection);
            GL.LoadIdentity();
            GL.Ortho(-1.0, 1.0, -1.0, 1.0, 0.0, 4.0);
        }
        #endregion

        #region OnUpdateFrame
        protected override void OnUpdateFrame(FrameEventArgs e)
        {
        }
        #endregion

        #region OnRenderFrame
        protected override void OnRenderFrame(FrameEventArgs e)
        {
            GL.Clear(ClearBufferMask.ColorBufferBit);
            GL.Begin(PrimitiveType.Triangles);
            GL.Color3(Color.MidnightBlue);
            GL.Vertex2(-1.0f, 1.0f);
            GL.Color3(Color.SpringGreen);
            GL.Vertex2(0.0f, -1.0f);
            GL.Color3(Color.Ivory);
            GL.Vertex2(1.0f, 1.0f);
            GL.End();
            this.SwapBuffers();
        }
        #endregion
        
        #region public static void Main2()
        [STAThread]
        public static void Main2()
        {
            using (SimpleWindow example = new SimpleWindow())
            {
                // Utilities.SetWindowTitle(example);
                example.Run(30.0, 0.0);
            }
        }
        #endregion
    }
}
