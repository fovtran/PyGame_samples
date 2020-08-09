#version 130

// varying vec2 InTexCoords;
uniform sampler2D tex;
varying vec2 vTexCoord;

//in vec4 newColor;

// out vec4 x;
// out vec4 y;

void main() {
	gl_FragColor = texture2D(tex, vTexCoord);
	// newColor = vec4(0.0,1.0,0.0,0.5);
}
