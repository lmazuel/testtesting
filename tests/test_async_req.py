from package.async_client import AsyncClient

import pytest

@pytest.mark.asyncio
async def test_get():
    client = AsyncClient()
    assert "Python" in await client.get('http://python.org')