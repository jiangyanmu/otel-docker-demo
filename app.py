from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# 設定 Tracer Provider
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# OTLP exporter (送到 Collector)
otlp_exporter = OTLPSpanExporter(insecure=True)
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(otlp_exporter))

# Console exporter (直接印在終端)
console_exporter = ConsoleSpanExporter()
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(console_exporter))

# 建立範例 trace
with tracer.start_as_current_span("main-task"):
    print("Main task started...")
    with tracer.start_as_current_span("sub-task"):
        print("Doing sub-task...")
    print("Main task finished.")
