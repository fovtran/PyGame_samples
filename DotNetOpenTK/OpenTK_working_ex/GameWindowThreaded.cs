using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.Threading;
using OpenTK;
using OpenTK.Graphics;
using OpenTK.Graphics.OpenGL;
using OpenTK.Input;

namespace Examples.Tutorial
{
    // [Example("GameWindow Threaded", ExampleCategory.OpenTK, "GameWindow", 3, Documentation = "GameWindowThreaded")]
    public class ThreadedRendering : GameWindow
    {
        bool viewport_changed = true;
        int viewport_width, viewport_height;
        bool position_changed = true;
        int position_x, position_y;
        float position_dx, position_dy;
        bool exit = false;
        Thread rendering_thread;
        object update_lock = new object();
        const float GravityAccel = -9.81f;
        struct Particle
        {
            public Vector2 Position;
            public Vector2 Velocity;
            public Color4 Color;
        }
        List<Particle> Particles = new List<Particle>();
        Random rand = new Random();

        public ThreadedRendering()
            : base(800, 600)
        {
            KeyDown += delegate(object sender, KeyboardKeyEventArgs e)
            {
                if (e.Key == Key.Escape)  this.Exit();
            };

            KeyUp += delegate(object sender, KeyboardKeyEventArgs e)
            {
                if (e.Key == Key.F11)
                    if (this.WindowState == WindowState.Fullscreen)
                        this.WindowState = WindowState.Normal;
                    else
                        this.WindowState = WindowState.Fullscreen;
            };

            Resize += delegate(object sender, EventArgs e)
            {
                // Note that we cannot call any OpenGL methods directly. What we can do is set
                // a flag and respond to it from the rendering thread.
                lock (update_lock)
                {
                    viewport_changed = true;
                    viewport_width = Width;
                    viewport_height = Height;
                }
            };

            Move += delegate(object sender, EventArgs e)
            {
                // Note that we cannot call any OpenGL methods directly. What we can do is set
                // a flag and respond to it from the rendering thread.
                lock (update_lock)
                {
                    position_changed = true;
                    position_dx = (position_x - X) / (float)Width;
                    position_dy = (position_y - Y) / (float)Height;
                    position_x = X;
                    position_y = Y;
                }
            };

            // Make sure initial position are correct, otherwise we'll give a huge
            // initial velocity to the balls.
            position_x = X;
            position_y = Y;
        }

        #region OnLoad
        protected override void OnLoad(EventArgs e)
        {
            Context.MakeCurrent(null); // Release the OpenGL context so it can be used on the new thread.
            rendering_thread = new Thread(RenderLoop);
            rendering_thread.IsBackground = true;
            rendering_thread.Start();
        }
        #endregion

        #region OnUnload
        protected override void OnUnload(EventArgs e)
        {
            exit = true; // Set a flag that the rendering thread should stop running.
            rendering_thread.Join();
            base.OnUnload(e);
        }
        #endregion

        #region OnUpdateFrame
        protected override void OnUpdateFrame(FrameEventArgs e) {}
        #endregion

        #region OnRenderFrame
        protected override void OnRenderFrame(FrameEventArgs e) { Thread.Sleep(1); }
        #endregion

        #region RenderLoop
        void RenderLoop()
        {
            MakeCurrent(); // The context now belongs to this thread. No other thread may use it!

            VSync = VSyncMode.On;

            for (int i = 0; i < 64; i++)
            {
                Particle p = new Particle();
                p.Position = new Vector2((float)rand.NextDouble() * 2 - 1, (float)rand.NextDouble() * 2 - 1);
                p.Color.R = (float)rand.NextDouble();
                p.Color.G = (float)rand.NextDouble();
                p.Color.B = (float)rand.NextDouble();
                Particles.Add(p);
            }

            // Since we don't use OpenTK's timing mechanism, we need to keep time ourselves;
            Stopwatch render_watch = new Stopwatch();
            Stopwatch update_watch = new Stopwatch();
            update_watch.Start();
            render_watch.Start();

            GL.ClearColor(Color.MidnightBlue);
            GL.Enable(EnableCap.DepthTest);
            GL.Enable(EnableCap.PointSmooth);
            GL.PointSize(16);

            while (!exit)
            {
                Update(update_watch.Elapsed.TotalSeconds);
                update_watch.Reset();
                update_watch.Start();

                Render(render_watch.Elapsed.TotalSeconds);
                render_watch.Reset(); //  Stopwatch may be inaccurate over larger intervals.
                render_watch.Start(); // Plus, timekeeping is easier if we always start counting from 0.

                SwapBuffers();
            }

            Context.MakeCurrent(null);
        }
        #endregion

        #region Update
        void Update(double time)
        {
            lock (update_lock)
            {
                if (position_changed)
                {
                    for (int i = 0; i < Particles.Count; i++)
                    {
                        Particle p = Particles[i];
                        p.Velocity += new Vector2(
                            16 * (position_dx + 0.05f * (float)(rand.NextDouble() - 0.5)),
                            32 * (position_dy + 0.05f * (float)(rand.NextDouble() - 0.5)));
                        Particles[i] = p;
                    }

                    position_changed = false;
                }
            }

            // For simplicity, we use simple Euler integration to simulate particle movement.
            for (int i = 0; i < Particles.Count; i++)
            {
                Particle p = Particles[i];

                p.Velocity.X = Math.Abs(p.Position.X) >= 1 ?-p.Velocity.X * 0.92f : p.Velocity.X * 0.97f;
                p.Velocity.Y = Math.Abs(p.Position.Y) >= 1 ? -p.Velocity.Y * 0.92f : p.Velocity.Y * 0.97f;
                if (p.Position.Y > -0.99)
                {
                    p.Velocity.Y += (float)(GravityAccel * time);
                }
                else
                {
                    if (Math.Abs(p.Velocity.Y) < 0.02)
                    {
                        p.Velocity.Y = 0;
                        p.Position.Y = -1;
                    }
                    else
                    {
                        p.Velocity.Y *= 0.9f;
                    }
                }

                p.Position += p.Velocity * (float)time;
                if (p.Position.Y <= -1)
                    p.Position.Y = -1;

                Particles[i] = p;
            }
        }
        #endregion

        #region Render
        public void Render(double time)
        {
            lock (update_lock)
            {
                if (viewport_changed)
                {
                    GL.Viewport(0, 0, viewport_width, viewport_height);
                    viewport_changed = false;
                }
            }

            Matrix4 perspective = Matrix4.CreateOrthographic(2, 2, -1, 1);
            GL.MatrixMode(MatrixMode.Projection);
            GL.LoadMatrix(ref perspective);

            GL.MatrixMode(MatrixMode.Modelview);
            GL.LoadIdentity();

            GL.Clear(ClearBufferMask.ColorBufferBit | ClearBufferMask.DepthBufferBit);

            GL.Begin(PrimitiveType.Points);
            foreach (Particle p in Particles)
            {
                GL.Color4(p.Color);
                GL.Vertex2(p.Position);
            }
            GL.End();
        }
        #endregion

        #region public static void Main()
        [STAThread]
        public static void Main() { using (GameWindow example = new ThreadedRendering()) { example.Run(); } }
        #endregion
    }
}
