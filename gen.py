import asyncio
from pyppeteer import launch

async def auto_join_and_connect():
    browser = await launch(headless=False, args=['--start-maximized'])
    page = await browser.newPage()
    await page.setViewport({'width': 1920, 'height': 1080})

    # Navigate to the testnet quest site
    await page.goto('https://testnet-quest.genlayerlabs.com/', {'waitUntil': 'networkidle2'})
    print("Page loaded")

    # Wait for the "Join" or "Connect" button to appear - replace selector as needed
    try:
        # Example selector for a "Join" button - update with actual selector
        join_button_selector = 'button.join-button'  # <-- Replace with actual selector
        await page.waitForSelector(join_button_selector, timeout=10000)
        await page.click(join_button_selector)
        print("Clicked Join button")

        # Wait for any wallet connect button or modal to appear
        connect_button_selector = 'button.connect-wallet'  # <-- Replace with actual selector
        await page.waitForSelector(connect_button_selector, timeout=10000)
        await page.click(connect_button_selector)
        print("Clicked Connect Wallet button")

        # If wallet popup or iframe appears, you may need to handle it here
        # For example, switch to popup or wait for wallet approval UI

        # Wait some time for connection to complete or confirmation element
        await asyncio.sleep(5)

        # Optionally take a screenshot after connection
        await page.screenshot({'path': 'testnet_quest_connected.png'})
        print("Screenshot taken after connection")

    except Exception as e:
        print(f"Error during join/connect process: {e}")

    await browser.close()

asyncio.get_event_loop().run_until_complete(auto_join_and_connect())
