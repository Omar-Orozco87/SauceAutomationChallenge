from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_setup():
    global url, validUsername, inValidUsername, password, logginWrapperId, idUserName,\
        idPassword, xpathLoginButton, xpathDivInventory, xpathMenuButton, xpathShoppingCartButton,\
        xpathShoppingPage, xpathAddFirstInventoryItem, xpathFirstItemInShoppingCartPage,\
        xpathCheckOutButton, xpathCheckOutInfoPage, xpathErrorValidationData,\
        xpathSummaryPage, xpathFirstInventoryItem, xpathCheckOutContinueButton
    url = 'https://www.saucedemo.com/'
    validUsername = 'standard_user'
    inValidUsername = 'standard'
    password = 'secret_sauce'
    logginWrapperId = "//div[@class='login_wrapper']"
    idUserName = 'user-name'
    idPassword = 'password'
    xpathLoginButton = "//input[@value='LOGIN']"
    xpathDivInventory = "//div[@id='contents_wrapper']"
    xpathMenuButton = "//button[text()='Open Menu']"
    xpathShoppingCartButton = "//div[@id='shopping_cart_container']/a"
    xpathShoppingPage = "//div[@id='cart_contents_container']"
    xpathAddFirstInventoryItem = "(//button[@class='btn_primary btn_inventory'])[1]"
    xpathFirstItemInShoppingCartPage = "(//div[@class='cart_list']/div[@class='cart_item'])[1]/div[@class='cart_quantity' and text()=1]"
    xpathCheckOutButton = "//a[@class='btn_action checkout_button']"
    xpathCheckOutInfoPage = "//div[@class='checkout_info_container']"
    xpathCartButton = "//input[@class='btn_primary cart_button']"
    xpathErrorValidationData = "//h3[@data-test='error']"
    xpathSummaryPage = "//div[@id='checkout_summary_container']"
    xpathFirstInventoryItem = "(//div[@class='inventory_item_name'])[1]"
    xpathCheckOutContinueButton = "//input[@class='btn_primary cart_button']"


def requestUrl(driver):
    driver.get(url)


def expectElementByXpath(xpath, wait):
    return wait.until(
        EC.presence_of_element_located((By.XPATH, xpath)))


def sendKeysById(driver, id, keys):
    driver.find_element_by_id(id).send_keys(keys)


def clickElementByXpath(driver, xpath):
    driver.find_element_by_xpath(xpath).click()


def addElementsToCart(driver, numberOfElements):
    for elementNumber in range(1, numberOfElements):
        clickElementByXpath(
            driver, "(//button[@class='btn_primary btn_inventory'])[" + str(elementNumber) + "]")


def verifyElementsAddedToCart(wait, numberOfElements):
    for elementNumber in range(1, numberOfElements):
        itemIsDisplayed = expectElementByXpath(
            "(//div[@class='cart_list']/div[@class='cart_item'])["+str(elementNumber)+"]/div[@class='cart_quantity' and text()=1]", wait)
        if not itemIsDisplayed:
            return False
    return True


def test_valid_user():
    testStatus = True
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    try:
        requestUrl(driver)
        logginWrapperIsLoaded = expectElementByXpath(
            logginWrapperId, wait)

        if not logginWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, idUserName, validUsername)
        sendKeysById(driver, idPassword, password)
        clickElementByXpath(driver, xpathLoginButton)

        contentsWrapperIsLoaded = expectElementByXpath(
            xpathDivInventory, wait)

        if not contentsWrapperIsLoaded:
            raise ValueError("Element expected was not found")

    except:
        testStatus = False
    finally:
        driver.close()
        driver.quit()
    assert testStatus


def test_inValid_user():
    testStatus = True
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    try:
        requestUrl(driver)
        logginWrapperIsLoaded = expectElementByXpath(
            logginWrapperId, wait)

        if not logginWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, idUserName, inValidUsername)
        sendKeysById(driver, idPassword, password)
        clickElementByXpath(driver, xpathLoginButton)

        errorMessage = expectElementByXpath(xpathErrorValidationData, wait)

        if not errorMessage:
            raise ValueError("Element expected was not found")

    except:
        testStatus = False
    finally:
        driver.close()
        driver.quit()
    assert testStatus


def test_LogOut_from_Products():

    testStatus = True
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    try:
        requestUrl(driver)
        logginWrapperIsLoaded = expectElementByXpath(
            logginWrapperId, wait)

        if not logginWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, idUserName, validUsername)
        sendKeysById(driver, idPassword, password)
        clickElementByXpath(driver, xpathLoginButton)

        contentsWrapperIsLoaded = expectElementByXpath(
            xpathDivInventory, wait)

        if not contentsWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        clickElementByXpath(driver, xpathMenuButton)

        menuIsLoaded = expectElementByXpath(
            "//div[@class='bm-menu']", wait)

        if not menuIsLoaded:
            raise ValueError("Element expected was not found")

        clickElementByXpath(driver, "//a[@id='logout_sidebar_link']")

        logginWrapperIsLoaded = expectElementByXpath(
            logginWrapperId, wait)

        if not logginWrapperIsLoaded:
            raise ValueError("Element expected was not found")

    except:
        testStatus = False
    finally:
        driver.close()
        driver.quit()
    assert testStatus


def test_navigate_to_shoppingCart():

    testStatus = True
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    try:
        requestUrl(driver)
        logginWrapperIsLoaded = expectElementByXpath(
            logginWrapperId, wait)

        if not logginWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, idUserName, validUsername)
        sendKeysById(driver, idPassword, password)
        clickElementByXpath(driver, xpathLoginButton)

        contentsWrapperIsLoaded = expectElementByXpath(
            xpathDivInventory, wait)

        if not contentsWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        clickElementByXpath(driver, xpathShoppingCartButton)

        shoppingCartPageIsLoaded = expectElementByXpath(
            xpathShoppingPage, wait)

        if not shoppingCartPageIsLoaded:
            raise ValueError("Element expected was not found")

    except:
        testStatus = False
    finally:
        driver.close()
        driver.quit()
    assert testStatus


def test_add1Item_to_shoppingCart():

    testStatus = True
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    try:
        requestUrl(driver)
        logginWrapperIsLoaded = expectElementByXpath(
            logginWrapperId, wait)

        if not logginWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, idUserName, validUsername)
        sendKeysById(driver, idPassword, password)
        clickElementByXpath(driver, xpathLoginButton)

        contentsWrapperIsLoaded = expectElementByXpath(
            xpathDivInventory, wait)

        if not contentsWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        clickElementByXpath(
            driver, xpathAddFirstInventoryItem)

        clickElementByXpath(driver, xpathShoppingCartButton)

        shoppingCartPageIsLoaded = expectElementByXpath(
            xpathShoppingPage, wait)

        if not shoppingCartPageIsLoaded:
            raise ValueError("Element expected was not found")

        oneItemIsDisplayed = expectElementByXpath(
            xpathFirstItemInShoppingCartPage, wait)

        if not oneItemIsDisplayed:
            raise ValueError("Element expected was not found")

    except:
        testStatus = False
    finally:
        driver.close()
        driver.quit()
    assert testStatus


def test_add_multiple_items_to_shoppingCart():
    testStatus = True
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    try:
        requestUrl(driver)
        logginWrapperIsLoaded = expectElementByXpath(
            logginWrapperId, wait)

        if not logginWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, idUserName, validUsername)
        sendKeysById(driver, idPassword, password)
        clickElementByXpath(driver, xpathLoginButton)

        contentsWrapperIsLoaded = expectElementByXpath(
            xpathDivInventory, wait)

        if not contentsWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        addElementsToCart(driver, 4)

        clickElementByXpath(driver, xpathShoppingCartButton)

        shoppingCartPageIsLoaded = expectElementByXpath(
            xpathShoppingPage, wait)

        if not shoppingCartPageIsLoaded:
            raise ValueError("Element expected was not found")

        allElementsAreListed = verifyElementsAddedToCart(wait, 4)

        if not allElementsAreListed:
            raise ValueError("Elements expected were not found")

    except:
        testStatus = False
    finally:
        driver.close()
        driver.quit()
    assert testStatus


def test_addItem_to_shoppingCart_with_no_zip_info():

    testStatus = True
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    try:
        requestUrl(driver)
        logginWrapperIsLoaded = expectElementByXpath(
            logginWrapperId, wait)

        if not logginWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, idUserName, validUsername)
        sendKeysById(driver, idPassword, password)
        clickElementByXpath(driver, xpathLoginButton)

        contentsWrapperIsLoaded = expectElementByXpath(
            xpathDivInventory, wait)

        if not contentsWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        clickElementByXpath(
            driver, xpathAddFirstInventoryItem)

        clickElementByXpath(driver, xpathShoppingCartButton)

        shoppingCartPageIsLoaded = expectElementByXpath(
            xpathShoppingPage, wait)

        if not shoppingCartPageIsLoaded:
            raise ValueError("Element expected was not found")

        oneItemIsDisplayed = expectElementByXpath(
            xpathFirstItemInShoppingCartPage, wait)

        if not oneItemIsDisplayed:
            raise ValueError("Element expected was not found")

        clickElementByXpath(driver, xpathCheckOutButton)

        checkOutYourInfoIsLoaded = expectElementByXpath(
            xpathCheckOutInfoPage, wait)

        if not checkOutYourInfoIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, "first-name", "testName")
        sendKeysById(driver, "last-name", "testLastName")

        clickElementByXpath(driver, xpathCheckOutContinueButton)

        errorZipCodeMesage = expectElementByXpath(
            xpathErrorValidationData, wait)

        if not errorZipCodeMesage:
            raise ValueError("Element expected was not found")

    except:
        testStatus = False
    finally:
        driver.close()
        driver.quit()
    assert testStatus


def test_navigates_overview_page():
    testStatus = True
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    try:
        requestUrl(driver)
        logginWrapperIsLoaded = expectElementByXpath(
            logginWrapperId, wait)

        if not logginWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, idUserName, validUsername)
        sendKeysById(driver, idPassword, password)
        clickElementByXpath(driver, xpathLoginButton)

        contentsWrapperIsLoaded = expectElementByXpath(
            xpathDivInventory, wait)

        if not contentsWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        clickElementByXpath(
            driver, xpathAddFirstInventoryItem)

        clickElementByXpath(driver, xpathShoppingCartButton)

        shoppingCartPageIsLoaded = expectElementByXpath(
            xpathShoppingPage, wait)

        if not shoppingCartPageIsLoaded:
            raise ValueError("Element expected was not found")

        oneItemIsDisplayed = expectElementByXpath(
            xpathFirstItemInShoppingCartPage, wait)

        if not oneItemIsDisplayed:
            raise ValueError("Element expected was not found")

        clickElementByXpath(driver, xpathCheckOutButton)

        checkOutYourInfoIsLoaded = expectElementByXpath(
            xpathCheckOutInfoPage, wait)

        if not checkOutYourInfoIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, "first-name", "testName")
        sendKeysById(driver, "last-name", "testLastName")
        sendKeysById(driver, "postal-code", "5555555")

        clickElementByXpath(
            driver, xpathCheckOutContinueButton)

        summaryContainerIsLoaded = expectElementByXpath(
            xpathSummaryPage, wait)

        if not summaryContainerIsLoaded:
            raise ValueError("Element expected was not found")

    except:
        testStatus = False
    finally:
        driver.close()
        driver.quit()
    assert testStatus


def test_navigates_overview_page_and_item_matches():
    testStatus = True
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    try:
        requestUrl(driver)
        logginWrapperIsLoaded = expectElementByXpath(
            logginWrapperId, wait)

        if not logginWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, idUserName, validUsername)
        sendKeysById(driver, idPassword, password)
        clickElementByXpath(driver, xpathLoginButton)

        contentsWrapperIsLoaded = expectElementByXpath(
            xpathDivInventory, wait)

        if not contentsWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        clickElementByXpath(
            driver, xpathAddFirstInventoryItem)

        itemName = driver.find_element_by_xpath(
            xpathFirstInventoryItem).text

        clickElementByXpath(driver, xpathShoppingCartButton)

        shoppingCartPageIsLoaded = expectElementByXpath(
            xpathShoppingPage, wait)

        if not shoppingCartPageIsLoaded:
            raise ValueError("Element expected was not found")

        oneItemIsDisplayed = expectElementByXpath(
            xpathFirstItemInShoppingCartPage, wait)

        if not oneItemIsDisplayed:
            raise ValueError("Element expected was not found")

        clickElementByXpath(driver, xpathCheckOutButton)

        checkOutYourInfoIsLoaded = expectElementByXpath(
            xpathCheckOutInfoPage, wait)

        if not checkOutYourInfoIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, "first-name", "testName")
        sendKeysById(driver, "last-name", "testLastName")
        sendKeysById(driver, "postal-code", "5555555")

        clickElementByXpath(
            driver, xpathCheckOutContinueButton)

        summaryContainerIsLoaded = expectElementByXpath(
            xpathSummaryPage, wait)

        if not summaryContainerIsLoaded:
            raise ValueError("Element expected was not found")

        itemToPurchase = driver.find_element_by_xpath(
            xpathFirstInventoryItem).text

        if not itemName == itemToPurchase:
            testStatus = False

    except:
        testStatus = False
    finally:
        driver.close()
        driver.quit()
    assert testStatus


def test_complete_purchase():
    testStatus = True
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    try:
        requestUrl(driver)
        logginWrapperIsLoaded = expectElementByXpath(
            logginWrapperId, wait)

        if not logginWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, idUserName, validUsername)
        sendKeysById(driver, idPassword, password)
        clickElementByXpath(driver, xpathLoginButton)

        contentsWrapperIsLoaded = expectElementByXpath(
            xpathDivInventory, wait)

        if not contentsWrapperIsLoaded:
            raise ValueError("Element expected was not found")

        clickElementByXpath(
            driver, xpathAddFirstInventoryItem)

        itemName = driver.find_element_by_xpath(
            xpathFirstInventoryItem).text

        clickElementByXpath(driver, xpathShoppingCartButton)

        shoppingCartPageIsLoaded = expectElementByXpath(
            xpathShoppingPage, wait)

        if not shoppingCartPageIsLoaded:
            raise ValueError("Element expected was not found")

        oneItemIsDisplayed = expectElementByXpath(
            xpathFirstItemInShoppingCartPage, wait)

        if not oneItemIsDisplayed:
            raise ValueError("Element expected was not found")

        clickElementByXpath(driver, xpathCheckOutButton)

        checkOutYourInfoIsLoaded = expectElementByXpath(
            xpathCheckOutInfoPage, wait)

        if not checkOutYourInfoIsLoaded:
            raise ValueError("Element expected was not found")

        sendKeysById(driver, "first-name", "testName")
        sendKeysById(driver, "last-name", "testLastName")
        sendKeysById(driver, "postal-code", "5555555")

        clickElementByXpath(
            driver, xpathCheckOutContinueButton)

        summaryContainerIsLoaded = expectElementByXpath(
            xpathSummaryPage, wait)

        if not summaryContainerIsLoaded:
            raise ValueError("Element expected was not found")

        itemToPurchase = driver.find_element_by_xpath(
            xpathFirstInventoryItem).text

        if not itemName == itemToPurchase:
            raise ValueError("Element to purchase does not match")

        clickElementByXpath(
            driver, "//a[@class='btn_action cart_button' and text()='FINISH']")

        finishContainerIsLoaded = expectElementByXpath(
            "//div[@id='checkout_complete_container']", wait)

        if not finishContainerIsLoaded:
            raise ValueError("Element expected was not found")

    except:
        testStatus = False
    finally:
        driver.close()
        driver.quit()
    assert testStatus
