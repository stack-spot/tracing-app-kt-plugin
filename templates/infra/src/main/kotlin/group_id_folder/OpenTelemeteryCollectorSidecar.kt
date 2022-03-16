{% if inputs.trace_exporter == 'AWS X-Ray' %}
package {{project_group_id}}

import org.cdk8s.plus22.ConfigMap
import org.cdk8s.plus22.ContainerProps
import org.cdk8s.plus22.Volume
import org.cdk8s.plus22.VolumeMount
import software.constructs.Construct
import java.nio.file.Paths

class OpenTelemeteryCollectorSidecar(scope: Construct) : ContainerProps {
    companion object {
        private const val CONFIG_NAME = "collector-config.yaml"
    }

    private val configMap = ConfigMap(scope, "collector-config")
    private val volumeMount = VolumeMount.builder()
        .path("/etc/otel.d")
        .volume(Volume.fromConfigMap(this.configMap))
        .build()

    init {
        this.configMap.addFile(Paths.get("..", CONFIG_NAME).toString())
    }

    override fun getArgs(): List<String> = listOf("--config=${this.volumeMount.path}/$CONFIG_NAME")

    override fun getImage(): String = "public.ecr.aws/aws-observability/aws-otel-collector"

    override fun getName(): String = "aws-otel-collector"

    override fun getVolumeMounts(): List<VolumeMount> = listOf(this.volumeMount)
}
{% endif %}
