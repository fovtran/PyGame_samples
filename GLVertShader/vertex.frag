#version 130

in vec4 position;
varying vec4 vTexCoord;
uniform sampler2D tex;
out vec2 color;

void main() {
	color = texture(tex,position);
	//gl_FragColor = texture2D(tex, vTexCoord);
	//x = texture2D(tex, vTexCoord);
	// newColor = vec4(0.0,1.0,0.0,0.5);
}
