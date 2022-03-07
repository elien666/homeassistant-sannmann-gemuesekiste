# View Sannmann Gemüsekisten Weekly Content in Homeassistant

... work in progress ...

## Install

1. Clone
2. Copy ```custom_components/sannmann_gemuese``` into ```config/custom_components/```
3. Add ```sannmann_gemuese:``` into ```config/configuration.yaml```
4. Restart Homeassistant

## Dashboard

Example card:

```yaml
type: markdown
title: Gemüsekiste
content: >-
  {% if state_attr('sensor.sannmann_gemuesekiste_regional_mittel', 'this_week') != '' %}
    ### Diese Woche
    {{ state_attr('sensor.sannmann_gemuesekiste_regional_mittel', 'this_week') }}
  {% endif %}

  {% if state_attr('sensor.sannmann_gemuesekiste_regional_mittel', 'next_week' != '') %}
    ### Nächste Woche
    {{ state_attr('sensor.sannmann_gemuesekiste_regional_mittel', 'next_week') }}
  {% endif %}
```

![Dashboard Example Card](doc/dasboard-card-example.png)

![Exceprt of sensor states provided by this integration](doc/states.png)