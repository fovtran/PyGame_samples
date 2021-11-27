using System;

﻿namespace Examples.WinForms
{
    partial class GameLoopForm
    {
        private System.ComponentModel.IContainer components = null;
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null)) { components.Dispose(); }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code
        private void InitializeComponent()
        {
          System.Reflection.Assembly a=null;

          try{
            a = System.Reflection.Assembly.Load("opentk.glcontrol.dll");
            } catch(Exception e) { System.Console.WriteLine("Error Loading DLL", e.ToString()); }

            // Get the type to use.
            System.Type myType = a.GetType("OpenTK");
            // Get the method to call.
            System.Reflection.MethodInfo myMethod = myType.GetMethod("GLControl");
            // Create an instance.
            object obj = System.Activator.CreateInstance(myType);
            // Execute the method.
            myMethod.Invoke(obj, null);
            // this.glControl = new OpenTK.GLControl();
            this.glControl = obj;
            this.SuspendLayout();
            //
            // glControl
            //
            this.glControl.BackColor = System.Drawing.Color.Black;
            this.glControl.Dock = System.Windows.Forms.DockStyle.Fill;
            this.glControl.Location = new System.Drawing.Point(0, 0);
            this.glControl.Name = "glControl";
            this.glControl.Size = new System.Drawing.Size(784, 564);
            this.glControl.TabIndex = 0;
            this.glControl.VSync = false;
            //
            // W02_Immediate_Mode_Cube
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(784, 564);
            this.Controls.Add(this.glControl);
            this.Name = "W02_Immediate_Mode_Cube";
            this.Text = "Cube";
            this.ResumeLayout(false);
        }
        #endregion

        private OpenTK.GLControl glControl;
    }
}
