import asyncio

from web3 import AsyncHTTPProvider, AsyncWeb3


async def main():
    w3 = AsyncWeb3(
        AsyncHTTPProvider("https://rpc.ankr.com/flare"),
    )
    chain_id = await w3.eth.chain_id
    print(f"Chain ID: {chain_id}")
    # Chain ID: 14
    return chain_id


if __name__ == "__main__":
    asyncio.run(main())
