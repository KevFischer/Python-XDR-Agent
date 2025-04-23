import etw, time, requests


class FileCollector:
    
    
    def __init__(self, providers: list[str], guids: list[str], attributes: list[str]) -> None:
        self.file_handle_cache: list[dict] = []
        self.attributes: list[str] = attributes
        self.providers: list[etw.ProviderInfo] = []
        if len(providers) != len(guids):
            raise Exception("Amount of providers and GUID's must be the same!")
        for i in range(len(providers)):
            self.providers.append(
                etw.ProviderInfo(providers[i], etw.GUID(guids[i]))
            )
        self.job: etw.ETW = etw.ETW(providers=self.providers, event_callback=self.event_callback)
            
    
    def event_callback(self, event: tuple) -> None:
        data: dict = {key: event[1].get(key, None) for key in self.attributes}
        print(data)
        
        
    def run(self) -> None:
        self.job.start()
        time.sleep(0.1)
        self.job.stop()
            
            
if __name__ == "__main__":
    collector: FileCollector = FileCollector(["Microsoft-Windows-Kernel-File"], ["{EDD08927-9CC4-4E65-B970-C2560FB5C289}"], ["EventHeader", "Task Name", "Irp", "FileObject", "FileKey", "FileName"])
    collector.run()