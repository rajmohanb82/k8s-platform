{{- define "platformops.name" -}}
{{- .Chart.Name -}}
{{- end -}}

{{- define "platformops.fullname" -}}
{{- .Release.Name -}}
{{- end -}}

{{- define "platformops.selectorLabels" -}}
app.kubernetes.io/name: {{ include "platformops.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}
