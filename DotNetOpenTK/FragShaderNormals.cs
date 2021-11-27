objectShader.Use();

objectShader.SetVector3("material.ambient", new Vector3(1.0f, 0.5f, 0.31f));
objectShader.SetVector3("material.diffuse", new Vector3(1.0f, 0.5f, 0.31f));
objectShader.SetVector3("material.specular", new Vector3(0.5f, 0.5f, 0.5f));

objectShader.SetVector3("light.position", new Vector3(100f, 1.0f, 2.0f));
objectShader.SetVector3("light.ambient", new Vector3(1.0f));
objectShader.SetVector3("light.diffuse", new Vector3(0.5f));
objectShader.SetVector3("light.specular", new Vector3(1.0f));

objectShader.SetMatrix4("view", Camera.GetViewMatrix());
objectShader.SetMatrix4("projection", Camera.GetProjectionMatrix());

// Vertex shader
#version 420 core

layout (location = 0) in vec3 aPosition;
layout (location = 1) in vec3 aNormal;
layout (location = 2) in vec2 aTexCoord;

out vec2 texCoord;
out vec3 FragPos;
out vec3 Normal;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

void main(void)
{
    texCoord = aTexCoord;
    FragPos = vec3(vec4(aPosition, 1.0) * model);
    Normal = -aNormal * mat3(transpose(inverse(model)));

    gl_Position = vec4(aPosition, 1.0) * model * view * projection;
}

// Shader
#version 420 core

in vec3 FragPos;
in vec3 Normal;
in vec2 texCoord;

out vec4 FragColor;

uniform sampler2D texture0;
uniform sampler2D texture1;

struct Material {
    sampler2D diffuse;
    sampler2D specular;
    float     shininess;
};
struct Light {
    vec3 position;
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
};

uniform Material material;
uniform Light light;
uniform vec3 viewPos;

void main()
{
    // Ambient
    vec3 ambient = light.ambient * vec3(texture(material.diffuse, texCoord));

    // Diffuse
    vec3 norm = normalize(Normal);
    vec3 lightDir = normalize(vec3(light.position - FragPos));
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = light.diffuse * diff * vec3(texture(material.diffuse, texCoord));

    // Specular
    vec3 viewDir = normalize(viewPos - FragPos);
    vec3 reflectDir = reflect(-lightDir, norm);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), material.shininess);
    vec3 specular = light.specular * spec * vec3(texture(material.specular, texCoord));

    vec3 result = ambient + diffuse + specular;
    FragColor = vec4(result, 1.0);
}

// Render
public void Render()
   {
       GL.Clear(ClearBufferMask.ColorBufferBit | ClearBufferMask.DepthBufferBit);

       if (Shapes == null || Shapes.Length == 0)
           return;

       IntPtr offset = (IntPtr)0;
       foreach (GLShape shape in Shapes)
       {
           ApplyTextures(shape);

           ApplyModelTransforms(shape, out Matrix4 model);
           objectShader.SetMatrix4("model", model);

           GL.DrawElements(PrimitiveType.Triangles, shape.Indices.Length, DrawElementsType.UnsignedInt, offset);
           offset += shape.IndexBufferSize;
       }

       objectShader.SetVector3("material.ambient", new Vector3(1.0f, 0.5f, 0.31f));
       objectShader.SetVector3("material.diffuse", new Vector3(1.0f, 0.5f, 0.31f));
       objectShader.SetVector3("material.specular", new Vector3(0.5f, 0.5f, 0.5f));

       objectShader.SetVector3("light.position", new Vector3(100f, 1.0f, 2.0f));
       objectShader.SetVector3("light.ambient", new Vector3(1.0f));
       objectShader.SetVector3("light.diffuse", new Vector3(0.5f));
       objectShader.SetVector3("light.specular", new Vector3(1.0f));

       objectShader.SetMatrix4("view", Camera.GetViewMatrix());
       objectShader.SetMatrix4("projection", Camera.GetProjectionMatrix());
       objectShader.Use();
   }

// Shader compiler
private void SetupObjectShader()
   {
       string vertexPath = Path.Combine(Environment.CurrentDirectory, @"GLSL\", "Vertex.vert");
       string fragmentPath = Path.Combine(Environment.CurrentDirectory, @"GLSL\", "Fragment.frag");

       objectShader = new Shader(vertexPath, fragmentPath);
       objectShader.Use();

       int vertexLocation = objectShader.GetAttribLocation("aPosition");
       GL.EnableVertexAttribArray(vertexLocation);
       GL.VertexAttribPointer(
           vertexLocation,
           3,
           VertexAttribPointerType.Float,
           false,
           8 * sizeof(float),
           0);

       int normCoordLocation = objectShader.GetAttribLocation("aNormal");
       GL.EnableVertexAttribArray(normCoordLocation);
       GL.VertexAttribPointer(
           normCoordLocation,
           3,
           VertexAttribPointerType.Float,
           false,
           8 * sizeof(float),
           3 * sizeof(float));


       int texCoordLocation = objectShader.GetAttribLocation("aTexCoord");
       GL.EnableVertexAttribArray(texCoordLocation);
       GL.VertexAttribPointer(
           texCoordLocation,
           2,
           VertexAttribPointerType.Float,
           false,
           8 * sizeof(float),
           6 * sizeof(float));

       objectShader.SetInt("texture0", 0);
       objectShader.SetInt("texture1", 1);
   }
   private void RecreateVertices()
      {
          List<float> vertices = new List<float>();

          float alpha = 2 * (float)Math.PI / rasterization;

          for (int i = 0; i < rasterization + 1; i++)
          {
              for (int j = 0; j < rasterization + 1; j++)
              {
                  float x = radius * (float)Math.Sin(i * alpha * 1.0) * (float)Math.Sin(j * alpha);
                  float y = radius * (float)Math.Sin(i * alpha * 1.0) * (float)Math.Cos(j * alpha);
                  float z = radius * (float)Math.Cos(i * alpha * 1.0);

                  float textureX = (float)j / rasterization;
                  float textureY = (float)i / rasterization * 2;

                  Vector3 normal = CreateNormal(x, y, z);

                  vertices.AddRange(new[] { x, y, z, normal[0], normal[1], normal[2], textureX, textureY });
              }
          }

          Vertices = vertices.ToArray();
      }

      private Vector3 CreateNormal(float x, float y, float z)
      {
          Vector3 normVector3 = new Vector3(x, y, z);
          normVector3.Normalize();

          return normVector3;
      }
