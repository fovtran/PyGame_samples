#version 330

in vec2 position;
in vec4 vTexCoord;
// in vec2 InTexCoords;
//uniform mat4 transform;

void main() {
	//vec4 vTexCoord = gl_MultiTexCoord0;
	//gl_Position = vTexCoord * vec4(position, 1.0f);
	gl_Position = vTexCoord;
}
