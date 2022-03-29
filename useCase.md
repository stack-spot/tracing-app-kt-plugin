## Execução do projeto criado

#### **Utilizando Jaeger**

Esse plugin entrega todas as configurações necessárias para que o Opentelemetry consiga exportar os tracings da aplicação ao Jaeger. As quais são:
- No `docker-compose` adiciona um contêiner do Jaeger e vincula o mesmo ao contêiner da aplicação.
- No `Dockerfile` adiciona o agente do [Opentelentry](https://github.com/open-telemetry/opentelemetry-java-instrumentation/) o qual será executado junto com o .jar da aplicação.

Veja o resultado na imagem abaixo:

![tracing-jaeger](/docs/image/tracing-with-jaeger.png)

#### **Utilizando X-Ray**

Esse plugin entrega todas as configurações necessárias para que o Opentelemetry consiga exportar os tracings da aplicação para o AWS X-Ray. As quais são:
- No `docker-compose` adiciona um contêiner do coletor da AWS e vincula o mesmo ao contêiner da aplicação. Mais informações acesso: [aws-otel-collector](https://aws-otel.github.io/docs/getting-started/collector).
- No `Dockerfile` adiciona o agente da [aws-opentelemetry](https://catalog.us-east-1.prod.workshops.aws/v2/workshops/31676d37-bbe9-4992-9cd1-ceae13c5116c/en-US/adot/javawalkthrough) o qual será executado junto com o .jar da aplicação.

Veja o resultado na imagem abaixo:

![tracing-xray](/docs/image/tracing-with-xray.png)

> Para usar o **AWS X-Ray** é necessário configurar as credenciais da **AWS** como variáveis de ambiente. O coletor do [aws-otel-collector](https://aws-otel.github.io/docs/getting-started/collector) precisa acessar as credenciais.
