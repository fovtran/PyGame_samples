#version 130

in vec2 position;
in vec4 vTexCoord;
uniform sampler2D tex;
out vec4 color;

void main() {
	color = texture(tex,position);
	//gl_FragColor = texture2D(tex, vTexCoord);
	//x = texture2D(tex, vTexCoord);
	//color = vec4(0.0,1.0,0.0,0.5);
}
