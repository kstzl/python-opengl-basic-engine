#version 330 core

layout (location=0) in vec3 vertexPos;

uniform mat4 projectionMatrix;
uniform mat4 viewMatrix;
uniform mat4 modelMatrix;

out vec3 fragPos;

void main() {
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPos, 1.0);

    fragPos = vec3(modelMatrix * vec4(vertexPos, 1.0));
} 