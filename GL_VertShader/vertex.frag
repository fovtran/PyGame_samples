#version 120

in vec3 newColor;
in vec2 OutTexCoords;

out vec4 outColor;
uniform sampler2D tex;

void main() {
	outColor = texture2D(tex, OutTexCoords);
	//gl_FragColor = outColor;
}
