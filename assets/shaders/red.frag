#version 330 core

uniform float time;

in vec3 fragPos;
in vec3 fragmentColor;

out vec4 color;

vec3 hsv2rgb(vec3 c)
{
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}


void main()
{
    // color = vec4(1, 0.1 * sin(time) * 5, 0.1, 1);
    float v = fragPos.x * 1 + fragPos.y * 1;
    color = vec4(hsv2rgb(vec3(time + v, 1, 1)), 1);
}