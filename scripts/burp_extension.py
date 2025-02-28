from burp import IBurpExtender, IScannerCheck, IScanIssue
import re

class BurpExtender(IBurpExtender, IScannerCheck):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Sensitive Data Finder")
        callbacks.registerScannerCheck(self)

    def doPassiveScan(self, baseRequestResponse):
        response = baseRequestResponse.getResponse()
        if response is None:
            return None

        responseStr = self._helpers.bytesToString(response)
        sensitive_patterns = [r'api_key=\w+', r'secret=\w+', r'token=\w{20,}']

        issues = []
        for pattern in sensitive_patterns:
            if re.search(pattern, responseStr):
                issues.append(CustomScanIssue(
                    baseRequestResponse.getHttpService(),
                    self._helpers.analyzeRequest(baseRequestResponse).getUrl(),
                    [baseRequestResponse],
                    "Sensitive Data Exposure",
                    "Found potential sensitive data in the response",
                    "High"
                ))

        return issues if issues else None

    def consolidateDuplicateIssues(self, existingIssue, newIssue):
        return 0 if existingIssue.getIssueName() == newIssue.getIssueName() else -1

class CustomScanIssue(IScanIssue):
    def __init__(self, httpService, url, httpMessages, name, detail, severity):
        self._httpService = httpService
        self._url = url
        self._httpMessages = httpMessages
        self._name = name
        self._detail = detail
        self._severity = severity

    def getUrl(self): return self._url
    def getIssueName(self): return self._name
    def getIssueDetail(self): return self._detail
    def getSeverity(self): return self._severity
    def getHttpMessages(self): return self._httpMessages
    def getHttpService(self): return self._httpService

