using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;
using System.Runtime.InteropServices;

using OpenTK;
using OpenTK.Graphics;
using OpenTK.Graphics.OpenGL;
using OpenTK.Platform;
using OpenTK.Platform.X11;
using OpenTK.Input;

namespace GlTest
{
    public class MainClass: GameWindow
    {
        public MainClass()
            : base(800, 600, new GraphicsMode(new ColorFormat(0, 0, 0, 0), 32, 0))
        {
            this.VSync = VSyncMode.Off;
        }

        public uint fbo;
        public uint textureA;
        public uint textureB;

        public int textureAWidth = 1024;
        public int textureAHeight = 1024;

        public int textureBWidth;
        public int textureBHeight;

        Random rand = new Random();

        #region Mouse_ButtonDown

        void Mouse_ButtonDown(object sender, MouseButtonEventArgs e)
        {
            if (e.Button == MouseButton.Left) {}
        }

        #endregion

        #region Mouse_Move

        void Mouse_Move(object sender, MouseMoveEventArgs e)
        {
            if (e.Mouse[MouseButton.Left]) {}
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
            else if (e.Key == Key.Enter) {}

            if (e.Key == Key.Space) {}
        }

        #endregion

        protected override void OnLoad(EventArgs e)
        {
          KeyDown += Keyboard_KeyDown;
          MouseMove += Mouse_Move;
          MouseDown += Mouse_ButtonDown;

            GL.Enable(EnableCap.Blend);
            GL.ShadeModel(ShadingModel.Smooth);
            GL.BlendFunc((BlendingFactor)BlendingFactorSrc.SrcAlpha, (BlendingFactor)BlendingFactorDest.OneMinusSrcAlpha);
            GL.Disable(EnableCap.DepthTest);
            GL.Disable(EnableCap.CullFace);

//            GL.PolygonMode(MaterialFace.Back, PolygonMode.Line);

            // Create Color Tex
            GL.GenTextures(1, out textureA);
            GL.BindTexture(TextureTarget.Texture2D, textureA);
            GL.TexImage2D(TextureTarget.Texture2D, 0, PixelInternalFormat.Rgba8, textureAWidth, textureAHeight, 0, OpenTK.Graphics.OpenGL.PixelFormat.Rgba, PixelType.UnsignedByte, IntPtr.Zero);
            GL.TexParameter(TextureTarget.Texture2D, TextureParameterName.TextureMinFilter, (int) TextureMinFilter.Linear);
            GL.TexParameter(TextureTarget.Texture2D, TextureParameterName.TextureMagFilter, (int) TextureMagFilter.Linear);
            GL.TexParameter(TextureTarget.Texture2D, TextureParameterName.TextureWrapS, (int) TextureWrapMode.ClampToBorder);
            GL.TexParameter(TextureTarget.Texture2D, TextureParameterName.TextureWrapT, (int) TextureWrapMode.ClampToBorder);

            GL.GenTextures(1, out textureB);
            GL.BindTexture(TextureTarget.Texture2D, textureB);

            Bitmap bmp = new Bitmap("MonaLisa.bmp");

            Console.WriteLine(textureBWidth = bmp.Width);
            Console.WriteLine(textureBHeight = bmp.Height);

            //get the data out of the bitmap
            System.Drawing.Imaging.BitmapData bmpBits = bmp.LockBits
            (
                new System.Drawing.Rectangle(0,0,textureBWidth, textureBHeight),
                System.Drawing.Imaging.ImageLockMode.ReadOnly,
                System.Drawing.Imaging.PixelFormat.Format32bppRgb
            );

            for (int row = 0; row < 1; row++)
            {
                for (int col = 0; col < 32; col++)
                {
                    Console.WriteLine
                    (
                        "{0}, {1}, {2}, {3}",
                        Marshal.ReadByte(bmpBits.Scan0, (row * textureBWidth + col) * 4 + 0),
                        Marshal.ReadByte(bmpBits.Scan0, (row * textureBWidth + col) * 4 + 1),
                        Marshal.ReadByte(bmpBits.Scan0, (row * textureBWidth + col) * 4 + 2),
                        Marshal.ReadByte(bmpBits.Scan0, (row * textureBWidth + col) * 4 + 3)
                    );

                }
            }

            Console.WriteLine(bmpBits.Width);
            Console.WriteLine(bmpBits.Height);


            GL.TexImage2D
            (
                TextureTarget.Texture2D,
                0,
                PixelInternalFormat.Rgba,
                textureBWidth,
                textureBHeight,
                0,
                OpenTK.Graphics.OpenGL.PixelFormat.Rgba,
                PixelType.UnsignedByte,
                bmpBits.Scan0
            );

//          GL.TexImage2D(TextureTarget.Texture2D, 0, PixelInternalFormat.Rgba8, textureBWidth, textureBHeight, 0, OpenTK.Graphics.OpenGL.PixelFormat.Rgba, PixelType.UnsignedByte, IntPtr.Zero);
            GL.TexParameter(TextureTarget.Texture2D, TextureParameterName.TextureMinFilter, (int) TextureMinFilter.Linear);
            GL.TexParameter(TextureTarget.Texture2D, TextureParameterName.TextureMagFilter, (int) TextureMagFilter.Linear);
            GL.TexParameter(TextureTarget.Texture2D, TextureParameterName.TextureWrapS, (int) TextureWrapMode.ClampToBorder);
            GL.TexParameter(TextureTarget.Texture2D, TextureParameterName.TextureWrapT, (int) TextureWrapMode.ClampToBorder);

            //free the bitmap data (we dont need it anymore because it has been passed to the OpenGL driver
            bmp.UnlockBits(bmpBits);

            // Create a FBO and attach the textures
            GL.Ext.GenFramebuffers(1, out fbo);
            GL.Ext.BindFramebuffer(FramebufferTarget.FramebufferExt, fbo);
            GL.Ext.FramebufferTexture2D(FramebufferTarget.FramebufferExt, FramebufferAttachment.ColorAttachment0Ext, TextureTarget.Texture2D, textureA, 0);

            #region Test for Error
            switch (GL.Ext.CheckFramebufferStatus(FramebufferTarget.FramebufferExt))
            {
            case FramebufferErrorCode.FramebufferCompleteExt:
                {
                    Console.WriteLine("FBO: The framebuffer is complete and valid for rendering.");
                    break;
                }
            case FramebufferErrorCode.FramebufferIncompleteAttachmentExt:
                {
                    Console.WriteLine("FBO: One or more attachment points are not framebuffer attachment complete. This could mean there’s no texture attached or the format isn’t renderable. For color textures this means the base format must be RGB or RGBA and for depth textures it must be a DEPTH_COMPONENT format. Other causes of this error are that the width or height is zero or the z-offset is out of range in case of render to volume.");
                    break;
                }
            case FramebufferErrorCode.FramebufferIncompleteMissingAttachmentExt:
                {
                    Console.WriteLine("FBO: There are no attachments.");
                    break;
                }
            /* case  FramebufferErrorCode.GL_FRAMEBUFFER_INCOMPLETE_DUPLICATE_ATTACHMENT_EXT:
                 {
                     Console.WriteLine("FBO: An object has been attached to more than one attachment point.");
                     break;
                 }*/
            case FramebufferErrorCode.FramebufferIncompleteDimensionsExt:
                {
                    Console.WriteLine("FBO: Attachments are of different size. All attachments must have the same width and height.");
                    break;
                }
            case FramebufferErrorCode.FramebufferIncompleteFormatsExt:
                {
                    Console.WriteLine("FBO: The color attachments have different format. All color attachments must have the same format.");
                    break;
                }
            case FramebufferErrorCode.FramebufferIncompleteDrawBufferExt:
                {
                    Console.WriteLine("FBO: An attachment point referenced by GL.DrawBuffers() doesn’t have an attachment.");
                    break;
                }
            case FramebufferErrorCode.FramebufferIncompleteReadBufferExt:
                {
                    Console.WriteLine("FBO: The attachment point referenced by GL.ReadBuffers() doesn’t have an attachment.");
                    break;
                }
            case FramebufferErrorCode.FramebufferUnsupportedExt:
                {
                    Console.WriteLine("FBO: This particular FBO configuration is not supported by the implementation.");
                    break;
                }
            default:
                {
                    Console.WriteLine("FBO: Status unknown. (yes, this is really bad.)");
                    break;
                }
            }

            // using FBO might have changed states, e.g. the FBO might not support stereoscopic views or double buffering
            int[] queryinfo = new int[6];
            GL.GetInteger(GetPName.MaxColorAttachmentsExt, out queryinfo[0]);
            GL.GetInteger(GetPName.AuxBuffers, out queryinfo[1]);
            GL.GetInteger(GetPName.MaxDrawBuffers, out queryinfo[2]);
            GL.GetInteger(GetPName.Stereo, out queryinfo[3]);
            GL.GetInteger(GetPName.Samples, out queryinfo[4]);
            GL.GetInteger(GetPName.Doublebuffer, out queryinfo[5]);
            Console.WriteLine("max. ColorBuffers: " + queryinfo[0] + " max. AuxBuffers: " + queryinfo[1] + " max. DrawBuffers: " + queryinfo[2] +
                               "\nStereo: " + queryinfo[3] + " Samples: " + queryinfo[4] + " DoubleBuffer: " + queryinfo[5]);

            Console.WriteLine("Last GL Error: " + GL.GetError());
            #endregion Test for Error


            GL.PushAttrib(AttribMask.ViewportBit);
            {
                GL.Viewport(0, 0, textureAWidth, textureAHeight);

                OpenTK.Matrix4 orthogonal = OpenTK.Matrix4.CreateOrthographicOffCenter(0, 1, 0, 1, -3, 3);
                GL.MatrixMode(MatrixMode.Projection);
                GL.LoadMatrix(ref orthogonal);

                Matrix4 lookat = Matrix4.LookAt(0, 0, 1, 0, 0, 0, 0, 1, 0);
                GL.MatrixMode(MatrixMode.Modelview);
                GL.LoadMatrix(ref lookat);


                // clear the screen in red, to make it very obvious what the clear affected. only the FBO, not the real framebuffer
                GL.ClearColor(0f, 0f, 0f, 0f);
                GL.Clear(ClearBufferMask.ColorBufferBit);

                // smack 50 random triangles into the FBO's textures
                GL.Begin(PrimitiveType.Triangles);
                {
                    for (int i = 0; i < 50; i++)
                    {
                        GL.Color4(((float)(rand.NextDouble())), ((float)(rand.NextDouble())), ((float)(rand.NextDouble())), ((float)(rand.NextDouble())));
                        GL.Vertex3(((float)(rand.NextDouble())), ((float)(rand.NextDouble())), 0);
                        GL.Color4(((float)(rand.NextDouble())), ((float)(rand.NextDouble())), ((float)(rand.NextDouble())), ((float)(rand.NextDouble())));
                        GL.Vertex3(((float)(rand.NextDouble())), ((float)(rand.NextDouble())), 0);
                        GL.Color4(((float)(rand.NextDouble())), ((float)(rand.NextDouble())), ((float)(rand.NextDouble())), ((float)(rand.NextDouble())));
                        GL.Vertex3(((float)(rand.NextDouble())), ((float)(rand.NextDouble())), 0);
                    }
                }
                GL.End();
            }
            GL.PopAttrib();
            GL.Ext.BindFramebuffer(FramebufferTarget.FramebufferExt, 0); // disable rendering into the FBO

            GL.ClearColor(1f, 1f, 1f, 0.0f);
            GL.Color3(1f, 1f, 1f);

            GL.Enable(EnableCap.Texture2D); // enable Texture Mapping
            GL.BindTexture(TextureTarget.Texture2D, 0); // bind default texture

//          IntPtr cglContext = Monobjc.OpenGL.CGL.GetCurrentContext();
//
//          IntPtr cglShareGroup = Monobjc.OpenGL.CGL.GetShareGroup(cglContext);
//
//          ManOCL.Context.ShareWithCGL(cglShareGroup);
//
//          Kernel kernel = ManOCL.Kernel.Create
//          (
//              "kernel1",
//              @"__kernel void kernel1(__global int *srcimg, __global int * output, __global int *smp)
//              {
//              }",
//              new Argument[]
//              {
//                  DeviceGlobalMemory.CreateFromArray(new int[1]),
//                  DeviceGlobalMemory.CreateFromArray(new int[2]),
//                  DeviceGlobalMemory.CreateFromArray(new int[1])
//              }
//          );

//          Console.WriteLine("Success!");
//          Console.WriteLine(kernel);
        }

        protected override void OnUnload(EventArgs e)
        {
            // Clean up what we allocated before exiting
            GL.DeleteTextures(1, ref textureA);
            GL.DeleteTextures(1, ref textureB);
            GL.Ext.DeleteFramebuffers(1, ref fbo);

            base.OnUnload(e);
        }

        protected override void OnResize (EventArgs e)
        {
            GL.Viewport(0, 0, Width, Height);

            double aspect_ratio = Width / (double)Height;

            OpenTK.Matrix4 perspective = OpenTK.Matrix4.CreatePerspectiveFieldOfView(MathHelper.PiOver4 * 3 / 2, (float)aspect_ratio, 1, 64);
            GL.MatrixMode(MatrixMode.Projection);
            GL.LoadMatrix(ref perspective);

            Matrix4 lookat = Matrix4.LookAt(0, 0, 3, 0, 0, 0, 0, 1, 0);
            GL.MatrixMode(MatrixMode.Modelview);
            GL.LoadMatrix(ref lookat);

            base.OnResize(e);
        }

        protected override void OnUpdateFrame (FrameEventArgs e)
        {
            base.OnUpdateFrame(e);
            //if (Keyboard[Key.Escape]) { this.Exit(); }
        }

        protected override void OnRenderFrame(FrameEventArgs e)
        {
            this.Title = "Frames per Second: " + (1.0 / e.Time);

            GL.Clear(ClearBufferMask.ColorBufferBit | ClearBufferMask.DepthBufferBit);

            GL.PushMatrix();
            {
                // Draw the Color Texture
                GL.Translate(-1f, 0f, 0f);
                GL.BindTexture(TextureTarget.Texture2D, textureA);
                GL.Begin(PrimitiveType.Quads);
                {
                    GL.TexCoord2(0f, 1f);
                    GL.Vertex2(-1.0f, 1.0f);
                    GL.TexCoord2(0.0f, 0.0f);
                    GL.Vertex2(-1.0f, -1.0f);
                    GL.TexCoord2(1.0f, 0.0f);
                    GL.Vertex2(1.0f, -1.0f);
                    GL.TexCoord2(1.0f, 1.0f);
                    GL.Vertex2(1.0f, 1.0f);
                }
                GL.End();

                GL.Translate(2f, 0f, 0f);
                GL.BindTexture(TextureTarget.Texture2D, textureB);
                GL.Begin(PrimitiveType.Quads);
                {
                    GL.TexCoord2(0f, 0f);
                    GL.Vertex2(-1.0f, 1.0f);

                    GL.TexCoord2(0.0f, 1.0f);
                    GL.Vertex2(-1.0f, -1.0f);

                    GL.TexCoord2(1.0f, 1.0f);
                    GL.Vertex2(1.0f, -1.0f);

                    GL.TexCoord2(1.0f, 0.0f);
                    GL.Vertex2(1.0f, 1.0f);
                }
                GL.End();
                GL.Translate(0f, 0f, 0f);
            }
            GL.PopMatrix();

            this.SwapBuffers();
        }

        #region public static void Main()

        /// <summary>
        /// Entry point of this example.
        /// </summary>
        [STAThread]
        public static void Main()
        {
          System.Console.WriteLine("Starting");

            using (MainClass example = new MainClass())
            {
                example.Title = "FrameBufferObjects";
                example.Run(1.0, 30.0);
            }
        }

        #endregion
    }
}
