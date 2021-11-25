using System;
using System.Collections.Generic;
using System.Drawing;
using OpenTK;
using OpenTK.Graphics.OpenGL;
using OpenTK.Input;

namespace Examples.Tutorial
{
    public class MouseCursorSimple : GameWindow
    {
        readonly MouseCursor MyCursor;
        List<Vector2> lines = new List<Vector2>();

        public MouseCursorSimple()
            : base(800, 600)
        {
            using (Bitmap bitmap = new Bitmap("Data/Textures/cursor.png"))
            {
                var data = bitmap.LockBits(
                    new Rectangle(0, 0, bitmap.Width, bitmap.Height),
                    System.Drawing.Imaging.ImageLockMode.ReadOnly,
                    System.Drawing.Imaging.PixelFormat.Format32bppPArgb);

                MyCursor = new OpenTK.MouseCursor(2, 21, data.Width, data.Height, data.Scan0);
                Cursor = MyCursor;
            }
            KeyDown += Keyboard_KeyDown;
            MouseMove += Mouse_Move;
            MouseDown += Mouse_ButtonDown;
        }

        void AddLine(float x, float y)
        {
            // Scale mouse coordinates from
            // (0, 0):(Width, Height) to
            // (-1, -1):(+1, +1)
            // Note, we must flip the y-coordinate
            // since mouse is reported with (0, 0)
            // at top-left and our projection uses
            // (-1, -1) at bottom left.
            x = (x- Width) / (float)Width;
            y = (Height - y) / (float)Height;
            lines.Add(new Vector2(2 * x + 1, 2 * y - 1));
        }

        #region Mouse_ButtonDown

        void Mouse_ButtonDown(object sender, MouseButtonEventArgs e)
        {
            if (e.Button == MouseButton.Left)
            {
                AddLine(e.X, e.Y);
            }
        }

        #endregion

        #region Mouse_Move

        void Mouse_Move(object sender, MouseMoveEventArgs e)
        {
            if (e.Mouse[MouseButton.Left])
            {
                AddLine(e.X, e.Y);
            }
        }
        #endregion

        #region Keyboard_KeyDown
        void Keyboard_KeyDown(object sender, KeyboardKeyEventArgs e)
        {
            if (e.Key == Key.Escape)
            {
                this.Exit();
            }

            if (e.Key == Key.Enter && e.Alt)
            {
                if (this.WindowState == WindowState.Fullscreen)
                    this.WindowState = WindowState.Normal;
                else
                    this.WindowState = WindowState.Fullscreen;
            }
            else if (e.Key == Key.Enter)
            {
                CursorVisible = !CursorVisible;
            }

            if (e.Key == Key.Space)
            {
                if (Cursor == MouseCursor.Default)
                {
                    Cursor = MyCursor;
                }
                else if (Cursor == MyCursor)
                {
                    Cursor = MouseCursor.Empty;
                }
                else
                {
                    Cursor = MouseCursor.Default;
                }
            }
        }

        #endregion

        #region OnLoad
        protected override void OnLoad(EventArgs e)
        {
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
            foreach (var p in lines)
            {
                GL.Color4(Color.White);
                GL.Vertex2(p);
            }
            GL.End();

            this.SwapBuffers();
        }
        #endregion

        #region public static void Main()
        [STAThread]
        public static void Main()
        {
            using (MouseCursorSimple example = new MouseCursorSimple())
            {
                // Utilities.SetWindowTitle(example);
                example.Run(30.0, 0.0);
            }
        }

        #endregion
    }
}
