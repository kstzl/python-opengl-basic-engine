#version 330 core

layout (location=0) in vec3 vertexPos;
layout (location=1) in vec3 vertexNormal;
layout (location=2) in vec3 vertexColor;
layout (location=3) in vec2 vertexCoord;

uniform mat4 projectionMatrix;
uniform mat4 viewMatrix;
uniform mat4 modelMatrix;

out vec3 normal;
out vec3 fragPos;
out vec3 fragmentColor;
out vec2 fragTexCoord;

void main() {
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPos, 1.0);

    fragmentColor = vertexColor;
    fragTexCoord = vertexCoord;
    fragPos = vec3(modelMatrix * vec4(vertexPos, 1.0));

    normal = mat3(transpose(inverse(modelMatrix))) * normalize(vertexNormal);
} 