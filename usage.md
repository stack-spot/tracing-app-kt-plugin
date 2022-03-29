## **Uso**

### **Pré-requisitos**
Para utilizar esse plugin é necessário instalar o cli do StackSpot, que você pode baixar [**aqui**](https://stackspot.com.br/).
Além disso, é importante já ter realizado a criação de um projeto utilizando **tracing-app-kt-plugin**

### **Como o rastreamento de plugin funciona?**

- OpenTelemetry é um conjunto de APIs, SDKs, ferramentas e integrações projetadas para a criação e gerenciamento de dados de telemetria, como o tracing.
    - Jaeger: Para que sejam enviadas informações ao Jaeger é necessário injetar na aplicação, via bytecode, o `agente` (.jar) fornecido pelo OpenTelemetry, pois ele é o resposável pela captura do tracing e também por receber as configurações do destino da sua exportação (Ex: Jaeger). Mais informações [acesse](https://github.com/open-telemetry/opentelemetry-java-instrumentation)
    - AWS X-Ray: Para que sejam enviadas informações ao AWS X-Ray é necessário injetar na aplicação, via bytecode, o `agente` (.jar) da AWS Opentemetry que será o responsável por receber e enviar o tracing para a cloud. Também é preciso criar um coletor, através do docker-compose (para execução local) que utilizará as informações de credenciais da AWS via variáveis de ambiente, ou um AWS distro (para implantação na cloud), fornecido via sidecar (CDK). Mais informações [acesse](https://aws-otel.github.io/docs/getting-started/collector/)