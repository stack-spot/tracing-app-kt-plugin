{% if inputs.trace_exporter == 'Jaeger' %}
ARG OPENTELEMETRY_JAR_FILE=https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v1.10.1/opentelemetry-javaagent.jar
ADD --chown=$USER ${OPENTELEMETRY_JAR_FILE} opentelemetry-javaagent.jar
ENV JAVA_TOOL_OPTIONS "-javaagent:opentelemetry-javaagent.jar -Dotel.service.name={{project_name}}"
{% elif inputs.trace_exporter == 'AWS X-Ray' %}
ARG AWS_OPENTELEMETRY_JAR=https://github.com/aws-observability/aws-otel-java-instrumentation/releases/latest/download/aws-opentelemetry-agent.jar
ADD --chown=$USER ${AWS_OPENTELEMETRY_JAR} aws-opentelemetry-agent.jar
ENV JAVA_TOOL_OPTIONS "-javaagent:aws-opentelemetry-agent.jar -Dotel.service.name={{project_name}}"
{% endif %}
