#version 330 core

in vec3 fragmentColor;
in vec2 fragTexCoord;
in vec3 normal;
in vec3 fragPos;

out vec4 color;

uniform sampler2D imageTexture;
uniform sampler2D normalMap;

uniform vec3 camPos;

struct Light
{
    vec3 position;
    vec3 ambient;
    vec3 diffuse;
    vec3 specular;
};

void main()
{
    // Light
    Light light = Light(vec3(2, 2, 4), vec3(0.5), vec3(0.2), vec3(0.5));

    // Normal
    vec3 normal_texture = texture(normalMap, fragTexCoord).rgb;

    vec3 Normal = normalize(normal_texture * 1);

    // Ambient
    vec3 ambient = light.ambient;

    // Diffuse
    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0, dot(lightDir, Normal));
    vec3 diffuse = diff * light.diffuse;

    // Specular
    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0), 32);
    vec3 specular = spec * light.specular;

    vec3 finalColor = vec3(1, 1, 1) * (ambient + diffuse + specular);

    float y = fragPos.y;
    color = vec4(finalColor, 1.0) * texture(imageTexture, fragTexCoord) - smoothstep(0, 3.5, y);;
}