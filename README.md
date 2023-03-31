# Tracing Plugin

- **Descrição:** O plugin [`tracing-app-kt-plugin`](https://github.com/stack-spot/tracing-app-kt-plugin.git) visa padronizar o *tracing* gerado pela aplicação utilizando OpenTelemetry para exportação.
- **Categoria:** Tracing.
- **Stack:** zup-kotlin-stack.
- **Criado em:** 31/01/2022.
- **Última atualização:** 18/03/2022.
- **Download:** https://github.com/stack-spot/tracing-app-kt-plugin.git


## **Visão Geral**
### **tracing-app-kt-plugin**

O **tracing-app-plugin** é um plugin que tem como objetivo padronizar o tracing gerado pelas aplicações, para que seja possível rastrear o passo a passo feito por cada aplicação. Ao adicionar o plugin na aplicação é possível escolher se o tracing será enviado para o [Jaeger](https://www.jaegertracing.io/) ou o [AWS X-Ray](https://aws.amazon.com/pt/xray/).

## **Uso**

### **Pré-requisitos**
Para utilizar esse plugin, é necessário ter uma stack Spring Kotlin criada através da Stack Spot CLI.

### **Aplicação**
Após gerar um projeto utilizando o **spring-app-kt-template**, acesse o diretório do projeto e aplique o **tracing-app-kt-plugin** através do comando:

```
stk apply plugin zup-kotlin-stack/tracing-app-kt-plugin
```

## **Configuração**

### **Inputs**
Os inputs necessários para utilizar o plugin são:

| **Campo** | **Valor** | **Descrição** |
| :--- | :--- | :--- |
| To which tool do you want to export traces?| AWS X-Ray/Jaeger | Escolha para qual ferramenta o *tracing* deverá ser exportado |

