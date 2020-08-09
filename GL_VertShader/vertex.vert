#version 130

in vec2 position;
in vec2 InTexCoords;

varying vec2 vTexCoord;

// uniform mat4 transform;

void main() {
	//gl_Position = transform * vec4(position, 1.0f);
	vTexCoord = gl_MultiTexCoord0;
	gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
	//OutTexCoords = InTexCoords;
}
