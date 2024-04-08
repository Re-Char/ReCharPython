import asyncio
import aiotieba
BDUSS = "pvejQ0aUFWRkp1UjY3TkZ6eEhJbkV0ODFjSXhkbzNvbWlVM0hqMUtZWVRrdnRsSVFBQUFBJCQAAAAAAQAAAAEAAABLkiAW1-7EqbXExu21uwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABMF1GUTBdRlRF"
txt = open("孙笑川吧数据.txt", "a", encoding="utf-8")


async def main():
    async with aiotieba.Client() as client:
        threads = await client.get_threads("孙笑川")
        for thread in threads:
            temp = await client.get_posts(thread.tid)
            arr = temp.objs
            txt.write(f"tid={thread.tid} title={thread.title}\ntext={thread.text}")
            for post in arr:
                txt.write(f"user_id={post.author_id} floor={post.floor}\ntext={post.contents}\n-----")
            txt.write('\n')
        print("ok...")


asyncio.run(main())
