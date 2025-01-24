import util.dynamics
import asyncio

async def main():
    await util.dynamics.get_user_dynamics(3546703753906662)

if __name__ == '__main__':
    asyncio.run(main())