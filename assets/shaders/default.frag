#version 330 core

in vec3 fragmentColor;
in vec2 fragTexCoord;
in vec3 normal;
in vec3 fragPos;

out vec4 color;

uniform sampler2D imageTexture;

void main()
{
    vec3 lightPos = vec3(2, 2, 5);
    vec3 lightColor = vec3(0, 0.1, 0.2) * 0.2;

    vec3 norm = normalize(normal);
    vec3 lightDir = normalize(lightPos - fragPos);  

    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    vec3 result = (0.5 + diffuse) * fragmentColor;

    float y = fragPos.y;
    color = vec4(result, 1.0) * texture(imageTexture, fragTexCoord) - smoothstep(0.0, 4, y);
}