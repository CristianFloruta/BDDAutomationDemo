Feature: Search functionality of ebay.com homepage

    @T1 @SimpleSearch5Tests
    Scenario Outline: Simple Search test for electronics in different categories
      Given Homepage: I am on ebay.com homepage
      When Homepage: I enter "<product_name>" on search bar
      And Homepage: I select "<category_name>" from all categories dropdown menu
      And Homepage: I click Search button
      Then ResultPage: Minimum 1000 results are retrieved
      Examples:
        | product_name | category_name |
        | iphone       | Cell Phones & Accessories |
        | ipad         | Computers/Tablets & Networking |
        | security     | Books              |
        | canon        | Cameras & Photo                |
        | toys         | Baby                           |

    @T2 @AdvancedSearch5Tests
    Scenario Outline:  Advanced Search test for clothing, shoes and accessories
      Given Homepage: I am on ebay.com homepage
      When Homepage: I click on Advanced search text link
      And AdvancedSearchPage: I enter "<product_name>" in Enter keyword or item number block
      And AdvancedSearchPage: I select "<keyword_choice>" from keyword option list
      And AdvancedSearchPage: I enter "<exclude_brand>" in Exclude words from your search
      And AdvancedSearchPage: I click Search button
      Then ResultPage: Minimum 1000 results are retrieved

      Examples:
        | product_name | keyword_choice | exclude_brand |
        | Shoes        | All words, any order | adidas  |
        | Tshirt       | Exact words, exact order | solomon |
        | cap     | Any words, any order     | columbia |
        | sweater      | Exact words, any order | reebok     |
        | hunting      | All words, any order   | nike     |

    @T3 @SoldItemsSearchTest
    Scenario: Advanced Search - SoldItemsSearchTest
      Given Homepage: I am on ebay.com homepage
      When Homepage: I click on Advanced search text link
      And AdvancedSearchPage: I enter iphone in Enter keyword or item number block
      And AdvancedSearchPage: I select Sold items from Search Including box
      And AdvancedSearchPage: I click Search button from page bottom
      Then ResultPage: Minimum 300 results are retrieved

    @T4 @BuyItNowSearchTest
      Scenario: Advanced Search - BuyItNowSearchTest
      Given Homepage: I am on ebay.com homepage
      When Homepage: I click on Advanced search text link
      And AdvancedSearchPage: I enter iphone in Enter keyword or item number block
      And AdvancedSearchPage: I select buy it now from Buying Format block
      And AdvancedSearchPage: I click Search button from page bottom
      Then ResultPage: Minimum 400 results are retrieved

    @T5 @NewItemSearchTest
      Scenario: Advanced Search - NewItemSearchTest
      Given Homepage: I am on ebay.com homepage
      When Homepage: I click on Advanced search text link
      And AdvancedSearchPage: I enter iphone in Enter keyword or item number block
      And AdvancedSearchPage: I select New from Condition block
      And AdvancedSearchPage: I click Search button from page bottom
      Then ResultPage: Minimum 500 results are retrieved

    @T6 @FreeReturnsSearchTest
      Scenario: Advanced Search - FreeReturnsSearchTest
      Given Homepage: I am on ebay.com homepage
      When Homepage: I click on Advanced search text link
      And AdvancedSearchPage: I enter iphone in Enter keyword or item number block
      And AdvancedSearchPage: I select Free returns from Show Results block
      And AdvancedSearchPage: I click Search button from page bottom
      Then ResultPage: Minimum 600 results are retrieved

    @T7 @UnspecifiedConditionSearchTest
      Scenario: Advanced Search - UnspecifiedConditionSearchTest
      Given Homepage: I am on ebay.com homepage
      When Homepage: I click on Advanced search text link
      And AdvancedSearchPage: I enter iphone in Enter keyword or item number block
      And AdvancedSearchPage: I select NotSpecified from Condition block
      And AdvancedSearchPage: I click Search button from page bottom
      Then ResultPage: Minimum 1 result is retrieved

    @T8 @LocationSearchTest
      Scenario: Advanced Search - LocationSearchTest
      Given Homepage: I am on ebay.com homepage
      When Homepage: I click on Advanced search text link
      And AdvancedSearchPage: I enter iphone in Enter keyword or item number block
      And AdvancedSearchPage: I select Worldwide from Item Location block
      And AdvancedSearchPage: I click Search button from page bottom
      Then ResultPage: Minimum 800 results are retrieved

    @T9 @LocationFilteredSearchTest
      Scenario: Advanced Search - LocationFilteredSearchTest
      Given Homepage: I am on ebay.com homepage
      When Homepage: I click on Advanced search text link
      And AdvancedSearchPage: I enter iphone in Enter keyword or item number block
      And AdvancedSearchPage: I select Available To from Item Location block
      And AdvancedSearchPage: I select United Kingdom
      And AdvancedSearchPage: I click Search button from page bottom
      Then ResultPage: Minimum 900 results are retrieved

    @T10 @ShippingOptionSearchTest
      Scenario: Advanced Search - ShippingOptionSearchTest
      Given Homepage: I am on ebay.com homepage
      When Homepage: I click on Advanced search text link
      And AdvancedSearchPage: I enter iphone in Enter keyword or item number block
      And AdvancedSearchPage: I select Free Shipping from Shipping Options block
      And AdvancedSearchPage: I click Search button from page bottom
      Then ResultPage: Minimum 100 results are retrieved