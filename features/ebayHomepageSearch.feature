Feature: Search functionality of ebay.com homepage

  Background:
    Given Homepage: I am on ebay.com homepage
    Then ResultPage: Minimum 1,000 results are retrieved

    @T1 @regressionTesting
    Scenario Outline: Simple Search test for electronics in different categories
      When Homepage: I enter "<product_name>" on search bar
      And Homepage: I select "<category_name>" from all categories dropdown menu
      And Homepage: I click Search button

      Examples:
        | product_name | category_name |
        | iphone       | Cell Phones & Accessories |
        | ipad         | Computers/Tablets & Networking |

    @T2 @sanityTesting
    Scenario Outline:  Advanced Search test for clothing, shoes and accessories
      When Homepage: I click on Advanced search text link
      And AdvancedSearchPage: I enter "<product_name>" in Enter keyword or item number block
      And AdvancedSearchPage: I select "<keyword_choice>" from keyword option list
      And AdvancedSearchPage: I enter "<exclude_brand>" in Exclude words from your search
      And AdvancedSearchPage: I select Clothing, Shoes & Accessories
      And AdvancedSearchPage: I click Search button

      Examples:
        | product_name | keyword_choice | exclude_brand |
        | Shoes        | All words, any order | adidas  |
        | Tshirt       | Exact words, exact order | red |


