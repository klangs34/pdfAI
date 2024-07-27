from langfuse.model import CreateTrace
from app.chat.tracing.langfuse import langfuse

class TraceableChain:
    def __call__(self, *args, **kwargs):
        # print(self.metadata)
        trace = langfuse.trace(
            CreateTrace(
                id=self.metadata["conversation_id"],
                metadata=self.metadata
            )
        )
        # print(kwargs)
        callbacks = kwargs.get("callbacks", [])
        # print(callbacks)
        if callbacks is None:
            callbacks = []
        callbacks.append(trace.getNewHandler())
        kwargs["callbacks"] = callbacks
        
        return super().__call__(*args, **kwargs)
        # pass