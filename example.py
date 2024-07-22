from visionLiveSDK3 import apiClient
from visionLiveSDK3.apiClient import ApiClient

appSecret = '{Your App Secret}'
appKey='{Your App Key}'
client = ApiClient('https://www.city.gov/API',appKey, appSecret)


eventResult = client.vision.cms.calendarcomponent.event.get(Fields=1, ID=1154)
dictEventResult = apiClient._O(dict(eventResult))
print(dictEventResult)
print((dictEventResult.Event.StartDate))


eventResult = client.vision.cms.core.system.content.get(Fields=1, ID=1154, ContentTypeName='Event')
dictEventResult = apiClient._O(dict(eventResult))
print(dictEventResult)
print((dictEventResult.Content.StartDate))

