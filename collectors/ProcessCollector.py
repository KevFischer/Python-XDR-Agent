import etw,time


class ProcessCollector:
    
    
    def __init__(self, providers: list[str], guids: list[str]) -> None:
        self.providers: list[etw.ProviderInfo] = []
        if len(providers) != len(guids):
            raise Exception("Amount of providers and GUID's must be the same!")
        for i in range(len(providers)):
            self.providers.append(
                etw.ProviderInfo(providers[i], etw.GUID(guids[i]))
            )
        self.job: etw.ETW = etw.ETW(providers=self.providers, event_callback=self.event_callback)
            
    
    def event_callback(self, event: tuple) -> None:
        print(event)
        
        
    def run(self) -> None:
        self.job.start()
        time.sleep(5)
        self.job.stop()
            
            
if __name__ == "__main__":
    collector: ProcessCollector = ProcessCollector(["Microsoft-Windows-Kernel-Process"], ["{22FB2CD6-0E7B-422B-A0C7-2FAD1FD0E716}"])
    collector.run()