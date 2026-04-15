import httpx

class API:
    def __init__(self):
        self.client = httpx.AsyncClient()
    # Use an asterisk * for the optional arguments since not every request has params, payload, and headers.
    async def request(self, method, url, *, params=None, payload=None, headers=None):
        response = await self.client.request(
            method=method,
            url=url,
            params=params,
            json=payload,
            headers=headers
        )
        print(f"Status Code: {response.status_code}")
        return response.json()

    async def get(self, url, params=None, headers=None):
        return await self.request("GET", url, params=params, headers=headers)

    async def post(self, url, payload=None, params=None, headers=None):
        return await self.request("POST", url, params=params, payload=payload, headers=headers)

    async def put(self, url, payload=None, params=None, headers=None):
        return await self.request("PUT", url, params=params, payload=payload, headers=headers)

    async def delete(self, url, payload=None, params=None, headers=None):
        return await self.request("DELETE", url, params=params, payload=payload, headers=headers)

    async def close(self):
        await self.client.aclose()
