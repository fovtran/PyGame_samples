// Copyright (c) 2013 Ashwin Nanjappa
using System;
using OpenTK;
using OpenTK.Graphics.OpenGL;
using OpenTK.Input;
using System;
using System.Drawing;
using System.Windows;
using System.Windows.Forms;
using System.Windows.Threading;

namespace TaoExample
{
    public class Program : GameWindow
    {
        public Program() : base(800, 600) {}

        #region OnLoad
        protected override void OnLoad(EventArgs e)
        {
            GL.Enable(Gl.GL_LIGHTING);
            GL.Enable(GL.GL_LIGHT0);
            float[] light_pos = new float[3] {1, 0.5F, 1};
            GL.Lightfv(GL.GL_LIGHT0, GL.GL_POSITION, light_pos);
            GL.Enable(GL.GL_DEPTH_TEST);
            GL.ClearColor(Color.MidnightBlue);
        }
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
        protected override void OnUpdateFrame(FrameEventArgs e) {}
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
            GL.Begin(PrimitiveType.LineStrip);
            /*
            foreach (var p in lines)
            {
                GL.Color4(Color.White);
                GL.Vertex2(p);
            }*/
            GL.End();
            this.SwapBuffers();
        }
        #endregion

        #region public static void Main()
        [STAThread]
        public static void Main()
        {
            using (Program example = new Program())
            {
                // Utilities.SetWindowTitle(example);
                example.Run(30.0, 0.0);
            }
        }
        #endregion
    }
}
