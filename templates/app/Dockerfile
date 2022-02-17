{% if inputs.trace_exporter == 'Jaeger' %}
ARG OPENTELEMETRY_JAR_FILE=https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/download/v1.10.1/opentelemetry-javaagent.jar
ADD --chown=1000 ${OPENTELEMETRY_JAR_FILE} opentelemetry-javaagent.jar
ENV JAVA_TOOL_OPTIONS "-javaagent:opentelemetry-javaagent.jar"
{% elif inputs.trace_exporter == 'Xray' %}
ARG AWS_OPENTELEMETRY_JAR=https://github.com/aws-observability/aws-otel-java-instrumentation/releases/latest/download/aws-opentelemetry-agent.jar
ADD --chown=1000 ${AWS_OPENTELEMETRY_JAR} aws-opentelemetry-agent.jar
ENV JAVA_TOOL_OPTIONS "-javaagent:aws-opentelemetry-agent.jar"
{% endif %}
