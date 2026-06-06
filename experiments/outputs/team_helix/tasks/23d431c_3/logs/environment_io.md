
### Environment Interaction 1
----------------------------------------------------------------------------
```python
print('=== ACTIVE TASK ==='); print(apis.supervisor.show_active_task())
print('=== ACCOUNT PASSWORDS (use these, never guess) ==='); print(apis.supervisor.show_account_passwords())
print('=== YOUR (SUPERVISOR) PROFILE ==='); print(apis.supervisor.show_profile())
print('=== AVAILABLE APPS ==='); print(apis.api_docs.show_app_descriptions())
```

```
=== ACTIVE TASK ===
{
 "instruction": "Buy me a watch from amazon within $110 (excluding tax). Only trust sellers I have ordered from in the past.",
 "status": null,
 "answer": "<<NOT_GIVEN>>"
}
=== ACCOUNT PASSWORDS (use these, never guess) ===
[
 {
  "account_name": "amazon",
  "password": "sQW-!iq"
 },
 {
  "account_name": "file_system",
  "password": "oD)7^7D"
 },
 {
  "account_name": "gmail",
  "password": "%2sQX_X"
 },
 {
  "account_name": "phone",
  "password": "2*oodVX"
 },
 {
  "account_name": "simple_note",
  "password": "c6yQ63t"
 },
 {
  "account_name": "splitwise",
  "password": "3-eG=xG"
 },
 {
  "account_name": "spotify",
  "password": "rO}t1vJ"
 },
 {
  "account_name": "todoist",
  "password": "u)(1oKU"
 },
 {
  "account_name": "venmo",
  "password": "^%Rz^Sj"
 }
]
=== YOUR (SUPERVISOR) PROFILE ===
{
 "first_name": "Chelsea",
 "last_name": "Burch",
 "email": "chelsea-burch@gmail.com",
 "phone_number": "7763361246",
 "birthday": "1992-03-22",
 "sex": "female"
}
=== AVAILABLE APPS ===
[
 {
  "name": "api_docs",
  "description": "An app to search and explore API documentation."
 },
 {
  "name": "supervisor",
  "description": "An app to access supervisor's personal information, account credentials, addresses, payment cards, and manage the assigned task."
 },
 {
  "name": "amazon",
  "description": "An online shopping app to buy products and manage orders, returns, etc."
 },
 {
  "name": "phone",
  "description": "An app to find and manage contact information for friends, family members, etc., send and receive messages, and manage alarms."
 },
 {
  "name": "file_system",
  "description": "A file system app to create and manage files and folders."
 },
 {
  "name": "spotify",
  "description": "A music streaming app to stream songs and manage song, album and playlist libraries."
 },
 {
  "name": "venmo",
  "description": "A social payment app to send, receive and request money to and from others."
 },
 {
  "name": "gmail",
  "description": "An email app to draft, send, receive, and manage emails."
 },
 {
  "name": "splitwise",
  "description": "A bill splitting app to track and split expenses with people."
 },
 {
  "name": "simple_note",
  "description": "A note-taking app to create and manage notes"
 },
 {
  "name": "todoist",
  "description": "A task management app to manage todo lists and collaborate on them with others."
 }
]
```


### Environment Interaction 2
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='amazon'))
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='login'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_verification_code",
  "description": "Send account verification code to your email address."
 },
 {
  "name": "verify_account",
  "description": "Verify your account using the verification code sent to your email address."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "show_product",
  "description": "Show product information based on its ID."
 },
 {
  "name": "search_sellers",
  "description": "Search for sellers with a query."
 },
 {
  "name": "show_seller",
  "description": "Show a detailed information about the seller."
 },
 {
  "name": "search_product_types",
  "description": "Search product types present in the database."
 },
 {
  "name": "show_product_feature_choices",
  "description": "Show the choices of colors, relative sizes and sellers aggregated over all products of the given product type. Because it's an aggregation, the choices may not be available for all products. If product type is not passed, it will return the choices for all products in the database."
 },
 {
  "name": "search_products",
  "description": "Search for products with a query and various filtering criteria."
 },
 {
  "name": "show_cart",
  "description": "show your cart."
 },
 {
  "name": "clear_cart",
  "description": "Clear your cart."
 },
 {
  "name": "add_product_to_cart",
  "description": "Add product by id and quantities to your cart."
 },
 {
  "name": "delete_product_from_cart",
  "description": "Remove a product from your cart."
 },
 {
  "name": "update_product_quantity_in_cart",
  "description": "Update product quantity in the user cart."
 },
 {
  "name": "apply_promo_code_to_cart",
  "description": "Apply a promo code to your cart."
 },
 {
  "name": "remove_promo_code_from_cart",
  "description": "Remove a promo code from your cart."
 },
 {
  "name": "show_wish_list",
  "description": "Get list of products in your wishlist."
 },
 {
  "name": "clear_wish_list",
  "description": "Clear wish list."
 },
 {
  "name": "add_product_to_wish_list",
  "description": "Add product by id and quantities to your wish list."
 },
 {
  "name": "delete_product_from_wish_list",
  "description": "Remove product from the user wish list."
 },
 {
  "name": "update_product_quantity_in_wish_list",
  "description": "Update product quantity in the user wish_list."
 },
 {
  "name": "move_product_from_cart_to_wish_list",
  "description": "Move product from the cart to the wish list."
 },
 {
  "name": "move_product_from_wish_list_to_cart",
  "description": "Move product from the wish list to the cart."
 },
 {
  "name": "add_gift_wrapping_to_product",
  "description": "Add gift wrapping to a product in your cart. If the product is already set to be gift wrapped, its quantity will be updated."
 },
 {
  "name": "remove_gift_wrapping_from_product",
  "description": "Remove gift wrapping from a product in your cart."
 },
 {
  "name": "show_orders",
  "description": "Show or search your past orders"
 },
 {
  "name": "place_order",
  "description": "Place an order for all the items in your cart."
 },
 {
  "name": "show_order",
  "description": "Get details of a past order."
 },
 {
  "name": "download_order_receipt",
  "description": "Download the receipt of a past order."
 },
 {
  "name": "show_payment_cards",
  "description": "Get a list of your payment_cards."
 },
 {
  "name": "add_payment_card",
  "description": "Add a new payment card."
 },
 {
  "name": "show_payment_card",
  "description": "Get details of a payment card."
 },
 {
  "name": "delete_payment_card",
  "description": "Delete payment card information."
 },
 {
  "name": "update_payment_card",
  "description": "Update payment card information."
 },
 {
  "name": "show_addresses",
  "description": "Get a list of your addresses."
 },
 {
  "name": "add_address",
  "description": "Add a new address."
 },
 {
  "name": "delete_address",
  "description": "Delete address information."
 },
 {
  "name": "update_address",
  "description": "Update address information."
 },
 {
  "name": "show_product_reviews",
  "description": "Get a list of product reviews."
 },
 {
  "name": "write_product_review",
  "description": "Write a product review."
 },
 {
  "name": "delete_product_review",
  "description": "Delete a product review."
 },
 {
  "name": "update_product_review",
  "description": "Update a product review."
 },
 {
  "name": "show_product_questions",
  "description": "Get a list of product questions."
 },
 {
  "name": "write_product_question",
  "description": "Post a question about a product."
 },
 {
  "name": "show_product_question_answers",
  "description": "Get a list of answers to a product question."
 },
 {
  "name": "write_product_question_answer",
  "description": "Write a answer to a product question."
 },
 {
  "name": "delete_product_question",
  "description": "Delete a product question."
 },
 {
  "name": "update_product_question",
  "description": "Update a product question."
 },
 {
  "name": "delete_product_question_answer",
  "description": "Delete a answer to a product question."
 },
 {
  "name": "update_product_question_answer",
  "description": "Update answer to a product question."
 },
 {
  "name": "show_returns",
  "description": "Get a list of your product returns."
 },
 {
  "name": "initiate_return",
  "description": "Initiate a product return."
 },
 {
  "name": "show_return",
  "description": "Show product return status."
 },
 {
  "name": "show_return_deliverers",
  "description": "Get a list of product return deliverers."
 },
 {
  "name": "show_prime_plans",
  "description": "Show information about prime plans available. Delivery fee is waived for prime members."
 },
 {
  "name": "show_prime_subscriptions",
  "description": "Show your prime subscription history."
 },
 {
  "name": "subscribe_prime",
  "description": "Subscribe to prime membership."
 },
 {
  "name": "download_prime_subscription_receipt",
  "description": "Download the receipt for a prime subscription."
 }
]
{
 "app_name": "amazon",
 "api_name": "login",
 "path": "/auth/token",
 "method": "POST",
 "description": "Login to your account.",
 "parameters": [
  {
   "name": "username",
   "type": "string",
   "required": true,
   "description": "Your account email.",
   "default": null,
   "constraints": []
  },
  {
   "name": "password",
   "type": "string",
   "required": true,
   "description": "Your account password.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "access_token": "string",
   "token_type": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 3
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='login'))
```

```
{
 "app_name": "amazon",
 "api_name": "login",
 "path": "/auth/token",
 "method": "POST",
 "description": "Login to your account.",
 "parameters": [
  {
   "name": "username",
   "type": "string",
   "required": true,
   "description": "Your account email.",
   "default": null,
   "constraints": []
  },
  {
   "name": "password",
   "type": "string",
   "required": true,
   "description": "Your account password.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "access_token": "string",
   "token_type": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 4
----------------------------------------------------------------------------
```python
amazon_password = [p for p in apis.supervisor.show_account_passwords() if p['account_name'] == 'amazon'][0]['password']
access_token = apis.amazon.login(username='chelsea-burch@gmail.com', password=amazon_password)['access_token']
print('Amazon access token:', access_token)
```

```
Amazon access token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbWF6b24rY2hlbHNlYS1idXJjaEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.D8wbFzXKo8bk0bJ-9n4hwB6ZLGJ7dauFTOdHbGg44lU
```


### Environment Interaction 5
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='amazon'))
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_order_history'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_order_history'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name show_order_history found for the amazon app. Check the api and app name again."}
```


### Environment Interaction 6
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='amazon'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_verification_code",
  "description": "Send account verification code to your email address."
 },
 {
  "name": "verify_account",
  "description": "Verify your account using the verification code sent to your email address."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "show_product",
  "description": "Show product information based on its ID."
 },
 {
  "name": "search_sellers",
  "description": "Search for sellers with a query."
 },
 {
  "name": "show_seller",
  "description": "Show a detailed information about the seller."
 },
 {
  "name": "search_product_types",
  "description": "Search product types present in the database."
 },
 {
  "name": "show_product_feature_choices",
  "description": "Show the choices of colors, relative sizes and sellers aggregated over all products of the given product type. Because it's an aggregation, the choices may not be available for all products. If product type is not passed, it will return the choices for all products in the database."
 },
 {
  "name": "search_products",
  "description": "Search for products with a query and various filtering criteria."
 },
 {
  "name": "show_cart",
  "description": "show your cart."
 },
 {
  "name": "clear_cart",
  "description": "Clear your cart."
 },
 {
  "name": "add_product_to_cart",
  "description": "Add product by id and quantities to your cart."
 },
 {
  "name": "delete_product_from_cart",
  "description": "Remove a product from your cart."
 },
 {
  "name": "update_product_quantity_in_cart",
  "description": "Update product quantity in the user cart."
 },
 {
  "name": "apply_promo_code_to_cart",
  "description": "Apply a promo code to your cart."
 },
 {
  "name": "remove_promo_code_from_cart",
  "description": "Remove a promo code from your cart."
 },
 {
  "name": "show_wish_list",
  "description": "Get list of products in your wishlist."
 },
 {
  "name": "clear_wish_list",
  "description": "Clear wish list."
 },
 {
  "name": "add_product_to_wish_list",
  "description": "Add product by id and quantities to your wish list."
 },
 {
  "name": "delete_product_from_wish_list",
  "description": "Remove product from the user wish list."
 },
 {
  "name": "update_product_quantity_in_wish_list",
  "description": "Update product quantity in the user wish_list."
 },
 {
  "name": "move_product_from_cart_to_wish_list",
  "description": "Move product from the cart to the wish list."
 },
 {
  "name": "move_product_from_wish_list_to_cart",
  "description": "Move product from the wish list to the cart."
 },
 {
  "name": "add_gift_wrapping_to_product",
  "description": "Add gift wrapping to a product in your cart. If the product is already set to be gift wrapped, its quantity will be updated."
 },
 {
  "name": "remove_gift_wrapping_from_product",
  "description": "Remove gift wrapping from a product in your cart."
 },
 {
  "name": "show_orders",
  "description": "Show or search your past orders"
 },
 {
  "name": "place_order",
  "description": "Place an order for all the items in your cart."
 },
 {
  "name": "show_order",
  "description": "Get details of a past order."
 },
 {
  "name": "download_order_receipt",
  "description": "Download the receipt of a past order."
 },
 {
  "name": "show_payment_cards",
  "description": "Get a list of your payment_cards."
 },
 {
  "name": "add_payment_card",
  "description": "Add a new payment card."
 },
 {
  "name": "show_payment_card",
  "description": "Get details of a payment card."
 },
 {
  "name": "delete_payment_card",
  "description": "Delete payment card information."
 },
 {
  "name": "update_payment_card",
  "description": "Update payment card information."
 },
 {
  "name": "show_addresses",
  "description": "Get a list of your addresses."
 },
 {
  "name": "add_address",
  "description": "Add a new address."
 },
 {
  "name": "delete_address",
  "description": "Delete address information."
 },
 {
  "name": "update_address",
  "description": "Update address information."
 },
 {
  "name": "show_product_reviews",
  "description": "Get a list of product reviews."
 },
 {
  "name": "write_product_review",
  "description": "Write a product review."
 },
 {
  "name": "delete_product_review",
  "description": "Delete a product review."
 },
 {
  "name": "update_product_review",
  "description": "Update a product review."
 },
 {
  "name": "show_product_questions",
  "description": "Get a list of product questions."
 },
 {
  "name": "write_product_question",
  "description": "Post a question about a product."
 },
 {
  "name": "show_product_question_answers",
  "description": "Get a list of answers to a product question."
 },
 {
  "name": "write_product_question_answer",
  "description": "Write a answer to a product question."
 },
 {
  "name": "delete_product_question",
  "description": "Delete a product question."
 },
 {
  "name": "update_product_question",
  "description": "Update a product question."
 },
 {
  "name": "delete_product_question_answer",
  "description": "Delete a answer to a product question."
 },
 {
  "name": "update_product_question_answer",
  "description": "Update answer to a product question."
 },
 {
  "name": "show_returns",
  "description": "Get a list of your product returns."
 },
 {
  "name": "initiate_return",
  "description": "Initiate a product return."
 },
 {
  "name": "show_return",
  "description": "Show product return status."
 },
 {
  "name": "show_return_deliverers",
  "description": "Get a list of product return deliverers."
 },
 {
  "name": "show_prime_plans",
  "description": "Show information about prime plans available. Delivery fee is waived for prime members."
 },
 {
  "name": "show_prime_subscriptions",
  "description": "Show your prime subscription history."
 },
 {
  "name": "subscribe_prime",
  "description": "Subscribe to prime membership."
 },
 {
  "name": "download_prime_subscription_receipt",
  "description": "Download the receipt for a prime subscription."
 }
]
```


### Environment Interaction 7
----------------------------------------------------------------------------
```python
print(apis.api_docs.search_api_docs(query='order'))
```

```
[
 {
  "app_name": "amazon",
  "api_name": "show_orders",
  "path": "/orders",
  "method": "GET",
  "description": "Show or search your past orders",
  "parameters": [
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   },
   {
    "name": "query",
    "type": "string",
    "required": false,
    "description": "Search query string.",
    "default": "",
    "constraints": []
   },
   {
    "name": "page_index",
    "type": "integer",
    "required": false,
    "description": "The index of the page to return.",
    "default": 0,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "page_limit",
    "type": "integer",
    "required": false,
    "description": "The maximum number of results to return per page.",
    "default": 5,
    "constraints": [
     "value >= 1.0, <= 20.0"
    ]
   },
   {
    "name": "sort_by",
    "type": "string",
    "required": false,
    "description": "The attribute to sort the orders by prefixed with +/- to reflect ascending/descending. Valid attributes: created_at. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page. If both query and sort_by are not given, null, or empty, sort_by will default to -created_at.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "order_id": 1,
     "address_id": 1,
     "payment_card_id": 1,
     "name": "string",
     "tax": 0.0,
     "delivery_fee": 0.0,
     "gift_wrap_fee": 0.0,
     "discount": 0.0,
     "created_at": "2019-01-01T00:00:00",
     "address_text": "string",
     "payment_card_digits": "string",
     "paid_amount": 0.0,
     "order_items": [
      {
       "product_id": 1,
       "ordered_quantity": 1,
       "returned_quantity": 1,
       "gift_wrap_quantity": 1,
       "price": 0.0,
       "expected_delivery_at": "2019-01-01T00:00:00",
       "delivered_at": "2019-01-01T00:00:00"
      }
     ]
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "amazon",
  "api_name": "show_order",
  "path": "/order/{order_id}",
  "method": "GET",
  "description": "Get details of a past order.",
  "parameters": [
   {
    "name": "order_id",
    "type": "integer",
    "required": true,
    "description": "ID of the order to be shown.",
    "default": null,
    "constraints": []
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "order_id": 1,
    "address_id": 1,
    "payment_card_id": 1,
    "name": "string",
    "tax": 0.0,
    "delivery_fee": 0.0,
    "gift_wrap_fee": 0.0,
    "discount": 0.0,
    "created_at": "2019-01-01T00:00:00",
    "address_text": "string",
    "payment_card_digits": "string",
    "paid_amount": 0.0,
    "order_items": [
     {
      "product_id": 1,
      "ordered_quantity": 1,
      "returned_quantity": 1,
      "gift_wrap_quantity": 1,
      "price": 0.0,
      "expected_delivery_at": "2019-01-01T00:00:00",
      "delivered_at": "2019-01-01T00:00:00"
     }
    ]
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "amazon",
  "api_name": "download_order_receipt",
  "path": "/order_receipt/{order_id}",
  "method": "GET",
  "description": "Download the receipt of a past order.",
  "parameters": [
   {
    "name": "order_id",
    "type": "integer",
    "required": true,
    "description": "ID of the order to download the receipt for.",
    "default": null,
    "constraints": []
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   },
   {
    "name": "download_to_file_path",
    "type": "string",
    "required": false,
    "description": "The file path to download the receipt file to in file system app. Path can be absolute, starting with '/', or relative to the user's home directory, starting with '~/'. If not passed, it will be saved in your ~/downloads directory.",
    "default": null,
    "constraints": []
   },
   {
    "name": "overwrite",
    "type": "boolean",
    "required": false,
    "description": "Whether to overwrite the file if it already exists.",
    "default": false,
    "constraints": []
   },
   {
    "name": "file_system_access_token",
    "type": "string",
    "required": false,
    "description": "Access token obtained from file_system app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string",
    "file_path": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "amazon",
  "api_name": "place_order",
  "path": "/orders",
  "method": "POST",
  "description": "Place an order for all the items in your cart.",
  "parameters": [
   {
    "name": "payment_card_id",
    "type": "integer",
    "required": true,
    "description": "ID of the payment card to use for this order.",
    "default": null,
    "constraints": []
   },
   {
    "name": "address_id",
    "type": "integer",
    "required": true,
    "description": "ID of the address used for shipping this order.",
    "default": null,
    "constraints": []
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string",
    "order_id": 1
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "show_song_queue",
  "path": "/music_player/song_queue",
  "method": "GET",
  "description": "Get the music player song queue. Songs are played in the order of the queue in a cycle.",
  "parameters": [
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from spotify app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "song_id": 1,
     "title": "string",
     "album_id": 1,
     "album_title": "string",
     "duration": 1,
     "artists": [
      {
       "id": 1,
       "name": "string"
      }
     ],
     "position": 1,
     "is_playing": true,
     "is_current": true
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 }
]
```


### Environment Interaction 8
----------------------------------------------------------------------------
```python
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbWF6b24rY2hlbHNlYS1idXJjaEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIwOTh9.D8wbFzXKo8bk0bJ-9n4hwB6ZLGJ7dauFTOdHbGg44lU'
orders = []
page_index = 0
while True:
    response = apis.amazon.show_orders(access_token=access_token, page_index=page_index)
    orders.extend(response)
    if len(response) < 5:  # page_limit default is 5
        break
    page_index += 1
print('Orders:', orders)
```

```
Orders: [{'order_id': 3146, 'address_id': 69, 'payment_card_id': 159, 'name': '1 watch', 'tax': 10.9, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2023-04-18T12:00:00', 'address_text': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'payment_card_digits': '5067', 'paid_amount': 119.9, 'order_items': [{'product_id': 1406, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 109.0, 'expected_delivery_at': '2023-04-20T18:32:29', 'delivered_at': '2023-04-20T18:32:29'}]}, {'order_id': 1029, 'address_id': 70, 'payment_card_id': 159, 'name': '2 cutting boards, 2 snorkel masks, 1 trekking pole', 'tax': 17.98, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2023-04-13T23:49:07', 'address_text': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'payment_card_digits': '5067', 'paid_amount': 197.78, 'order_items': [{'product_id': 401, 'ordered_quantity': 2, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 40.0, 'expected_delivery_at': '2023-04-19T19:18:01', 'delivered_at': '2023-04-19T19:18:01'}, {'product_id': 1610, 'ordered_quantity': 2, 'returned_quantity': 2, 'gift_wrap_quantity': 0, 'price': 24.9, 'expected_delivery_at': '2023-04-15T19:21:53', 'delivered_at': '2023-04-15T19:21:53'}, {'product_id': 2104, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 50.0, 'expected_delivery_at': '2023-04-16T19:47:13', 'delivered_at': '2023-04-16T19:47:13'}]}, {'order_id': 1013, 'address_id': 69, 'payment_card_id': 159, 'name': '2 dumbbells, 2 scissors, 1 kitchen timer, 1 umbrella stand', 'tax': 117.3, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2023-03-21T01:19:16', 'address_text': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'payment_card_digits': '5067', 'paid_amount': 1290.3, 'order_items': [{'product_id': 1295, 'ordered_quantity': 2, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 549.0, 'expected_delivery_at': '2023-03-23T18:04:21', 'delivered_at': '2023-03-23T18:04:21'}, {'product_id': 2213, 'ordered_quantity': 2, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 7.5, 'expected_delivery_at': '2023-03-24T18:58:55', 'delivered_at': '2023-03-24T18:58:55'}, {'product_id': 2339, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 20.0, 'expected_delivery_at': '2023-03-23T17:55:16', 'delivered_at': '2023-03-23T17:55:16'}, {'product_id': 2508, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 40.0, 'expected_delivery_at': '2023-03-26T17:10:47', 'delivered_at': '2023-03-26T17:10:47'}]}, {'order_id': 1019, 'address_id': 69, 'payment_card_id': 158, 'name': '2 mouse pads', 'tax': 10.0, 'delivery_fee': 0.0, 'gift_wrap_fee': 5.0, 'discount': 0.0, 'created_at': '2023-03-13T12:08:43', 'address_text': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'payment_card_digits': '9914', 'paid_amount': 115.0, 'order_items': [{'product_id': 1263, 'ordered_quantity': 2, 'returned_quantity': 2, 'gift_wrap_quantity': 1, 'price': 50.0, 'expected_delivery_at': '2023-03-18T18:56:41', 'delivered_at': '2023-03-18T18:56:41'}]}, {'order_id': 1018, 'address_id': 69, 'payment_card_id': 159, 'name': '2 sunglasses', 'tax': 30.8, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2023-02-09T17:03:50', 'address_text': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'payment_card_digits': '5067', 'paid_amount': 338.8, 'order_items': [{'product_id': 1432, 'ordered_quantity': 2, 'returned_quantity': 2, 'gift_wrap_quantity': 0, 'price': 154.0, 'expected_delivery_at': '2023-02-15T17:25:45', 'delivered_at': '2023-02-15T17:25:45'}]}, {'order_id': 1015, 'address_id': 69, 'payment_card_id': 157, 'name': '1 acoustic guitar, 1 face mask', 'tax': 331.0, 'delivery_fee': 0.0, 'gift_wrap_fee': 5.0, 'discount': 0.0, 'created_at': '2023-01-30T19:00:10', 'address_text': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'payment_card_digits': '5688', 'paid_amount': 3646.0, 'order_items': [{'product_id': 1494, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 1, 'price': 3300.0, 'expected_delivery_at': '2023-02-04T18:05:38', 'delivered_at': '2023-02-04T18:05:38'}, {'product_id': 2063, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 10.0, 'expected_delivery_at': '2023-02-01T17:38:59', 'delivered_at': '2023-02-01T17:38:59'}]}, {'order_id': 1034, 'address_id': 70, 'payment_card_id': 159, 'name': '1 disinfecting wipe, 1 cookware set, 1 smartphone', 'tax': 105.5, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2023-01-25T14:41:36', 'address_text': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'payment_card_digits': '5067', 'paid_amount': 1160.5, 'order_items': [{'product_id': 394, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 6.0, 'expected_delivery_at': '2023-01-29T18:13:13', 'delivered_at': '2023-01-29T18:13:13'}, {'product_id': 529, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 650.0, 'expected_delivery_at': '2023-02-01T19:37:56', 'delivered_at': '2023-02-01T19:37:56'}, {'product_id': 2410, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 399.0, 'expected_delivery_at': '2023-01-29T17:36:40', 'delivered_at': '2023-01-29T17:36:40'}]}, {'order_id': 1016, 'address_id': 69, 'payment_card_id': 159, 'name': '2 file folders, 1 wireless earbud, 1 hammer, 2 hairbrushes', 'tax': 36.99, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2023-01-11T12:59:05', 'address_text': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'payment_card_digits': '5067', 'paid_amount': 406.89, 'order_items': [{'product_id': 455, 'ordered_quantity': 2, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 13.0, 'expected_delivery_at': '2023-01-16T18:46:13', 'delivered_at': '2023-01-16T18:46:13'}, {'product_id': 733, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 299.9, 'expected_delivery_at': '2023-01-17T17:51:52', 'delivered_at': '2023-01-17T17:51:52'}, {'product_id': 1348, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 20.0, 'expected_delivery_at': '2023-01-13T19:28:02', 'delivered_at': '2023-01-13T19:28:02'}, {'product_id': 2468, 'ordered_quantity': 2, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 12.0, 'expected_delivery_at': '2023-01-15T19:45:37', 'delivered_at': '2023-01-15T19:45:37'}]}, {'order_id': 1028, 'address_id': 70, 'payment_card_id': 159, 'name': '1 acoustic guitar, 2 kitchen timers, 1 area rug', 'tax': 36.3, 'delivery_fee': 0.0, 'gift_wrap_fee': 5.0, 'discount': 0.0, 'created_at': '2022-12-25T23:36:33', 'address_text': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'payment_card_digits': '5067', 'paid_amount': 404.3, 'order_items': [{'product_id': 1492, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 1, 'price': 200.0, 'expected_delivery_at': '2023-01-01T18:13:02', 'delivered_at': '2023-01-01T18:13:02'}, {'product_id': 2342, 'ordered_quantity': 2, 'returned_quantity': 2, 'gift_wrap_quantity': 0, 'price': 7.0, 'expected_delivery_at': '2022-12-26T17:33:19', 'delivered_at': '2022-12-26T17:33:19'}, {'product_id': 2502, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 149.0, 'expected_delivery_at': '2022-12-28T18:16:16', 'delivered_at': '2022-12-28T18:16:16'}]}, {'order_id': 1022, 'address_id': 69, 'payment_card_id': 157, 'name': '1 GPS navigator, 1 ear protection, 1 office chair', 'tax': 130.4, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2022-12-01T10:36:35', 'address_text': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'payment_card_digits': '5688', 'paid_amount': 1434.4, 'order_items': [{'product_id': 65, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 300.0, 'expected_delivery_at': '2022-12-06T17:08:09', 'delivered_at': '2022-12-06T17:08:09'}, {'product_id': 571, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 25.0, 'expected_delivery_at': '2022-12-03T19:11:07', 'delivered_at': '2022-12-03T19:11:07'}, {'product_id': 633, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 979.0, 'expected_delivery_at': '2022-12-07T18:45:09', 'delivered_at': '2022-12-07T18:45:09'}]}, {'order_id': 1035, 'address_id': 70, 'payment_card_id': 159, 'name': '1 gaming keyboard, 1 telescope, 1 popcorn maker', 'tax': 63.0, 'delivery_fee': 0.0, 'gift_wrap_fee': 5.0, 'discount': 0.0, 'created_at': '2022-11-21T19:06:21', 'address_text': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'payment_card_digits': '5067', 'paid_amount': 698.0, 'order_items': [{'product_id': 436, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 200.0, 'expected_delivery_at': '2022-11-24T17:42:17', 'delivered_at': '2022-11-24T17:42:17'}, {'product_id': 1417, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 1, 'price': 400.0, 'expected_delivery_at': '2022-11-28T19:05:18', 'delivered_at': '2022-11-28T19:05:18'}, {'product_id': 2208, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 30.0, 'expected_delivery_at': '2022-11-25T17:30:13', 'delivered_at': '2022-11-25T17:30:13'}]}, {'order_id': 1027, 'address_id': 70, 'payment_card_id': 157, 'name': '2 cookbooks, 1 swimming goggle, 1 baseball cap', 'tax': 48.5, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2022-11-02T03:27:53', 'address_text': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'payment_card_digits': '5688', 'paid_amount': 533.5, 'order_items': [{'product_id': 428, 'ordered_quantity': 2, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 30.0, 'expected_delivery_at': '2022-11-04T18:24:03', 'delivered_at': '2022-11-04T18:24:03'}, {'product_id': 536, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 400.0, 'expected_delivery_at': '2022-11-04T19:57:09', 'delivered_at': '2022-11-04T19:57:09'}, {'product_id': 2080, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 25.0, 'expected_delivery_at': '2022-11-06T19:30:40', 'delivered_at': '2022-11-06T19:30:40'}]}, {'order_id': 1032, 'address_id': 70, 'payment_card_id': 158, 'name': '1 corkboard, 2 winter coats, 1 compass', 'tax': 39.3, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2022-10-17T14:31:18', 'address_text': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'payment_card_digits': '9914', 'paid_amount': 432.3, 'order_items': [{'product_id': 562, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 13.0, 'expected_delivery_at': '2022-10-18T17:17:29', 'delivered_at': '2022-10-18T17:17:29'}, {'product_id': 2245, 'ordered_quantity': 2, 'returned_quantity': 2, 'gift_wrap_quantity': 0, 'price': 160.0, 'expected_delivery_at': '2022-10-20T19:00:00', 'delivered_at': '2022-10-20T19:00:00'}, {'product_id': 2457, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 60.0, 'expected_delivery_at': '2022-10-18T17:35:32', 'delivered_at': '2022-10-18T17:35:32'}]}, {'order_id': 1021, 'address_id': 69, 'payment_card_id': 157, 'name': '2 water bottles, 1 cooling fan', 'tax': 5.58, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2022-10-15T11:32:15', 'address_text': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'payment_card_digits': '5688', 'paid_amount': 61.38, 'order_items': [{'product_id': 361, 'ordered_quantity': 2, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 19.9, 'expected_delivery_at': '2022-10-18T17:34:35', 'delivered_at': '2022-10-18T17:34:35'}, {'product_id': 2119, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 16.0, 'expected_delivery_at': '2022-10-17T18:35:43', 'delivered_at': '2022-10-17T18:35:43'}]}, {'order_id': 1014, 'address_id': 69, 'payment_card_id': 157, 'name': '2 golf clubs, 2 fire extinguishers', 'tax': 170.0, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2022-10-11T12:06:17', 'address_text': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'payment_card_digits': '5688', 'paid_amount': 1870.0, 'order_items': [{'product_id': 2589, 'ordered_quantity': 2, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 800.0, 'expected_delivery_at': '2022-10-12T19:55:34', 'delivered_at': '2022-10-12T19:55:34'}, {'product_id': 2655, 'ordered_quantity': 2, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 50.0, 'expected_delivery_at': '2022-10-15T17:25:23', 'delivered_at': '2022-10-15T17:25:23'}]}, {'order_id': 1020, 'address_id': 69, 'payment_card_id': 158, 'name': '2 cooling fans, 2 umbrella stands', 'tax': 31.0, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2022-09-25T14:12:36', 'address_text': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'payment_card_digits': '9914', 'paid_amount': 341.0, 'order_items': [{'product_id': 2120, 'ordered_quantity': 2, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 65.0, 'expected_delivery_at': '2022-10-02T17:46:48', 'delivered_at': '2022-10-02T17:46:48'}, {'product_id': 2511, 'ordered_quantity': 2, 'returned_quantity': 2, 'gift_wrap_quantity': 0, 'price': 90.0, 'expected_delivery_at': '2022-09-29T17:52:56', 'delivered_at': '2022-09-29T17:52:56'}]}, {'order_id': 1026, 'address_id': 70, 'payment_card_id': 159, 'name': '1 bath towel, 2 lawn mowers, 2 ski poles, 2 picture frames', 'tax': 84.4, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2022-09-15T18:05:18', 'address_text': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'payment_card_digits': '5067', 'paid_amount': 928.4, 'order_items': [{'product_id': 559, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 20.0, 'expected_delivery_at': '2022-09-16T18:00:44', 'delivered_at': '2022-09-16T18:00:44'}, {'product_id': 1205, 'ordered_quantity': 2, 'returned_quantity': 2, 'gift_wrap_quantity': 0, 'price': 349.0, 'expected_delivery_at': '2022-09-22T19:46:47', 'delivered_at': '2022-09-22T19:46:47'}, {'product_id': 1498, 'ordered_quantity': 2, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 50.0, 'expected_delivery_at': '2022-09-18T19:00:34', 'delivered_at': '2022-09-18T19:00:34'}, {'product_id': 1529, 'ordered_quantity': 2, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 13.0, 'expected_delivery_at': '2022-09-18T19:40:35', 'delivered_at': '2022-09-18T19:40:35'}]}, {'order_id': 1017, 'address_id': 69, 'payment_card_id': 159, 'name': '1 flute, 1 electric shaver, 2 medicine balls', 'tax': 155.3, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2022-08-31T17:34:08', 'address_text': '46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473', 'payment_card_digits': '5067', 'paid_amount': 1708.3, 'order_items': [{'product_id': 18, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 1300.0, 'expected_delivery_at': '2022-09-03T19:56:44', 'delivered_at': '2022-09-03T19:56:44'}, {'product_id': 2300, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 80.0, 'expected_delivery_at': '2022-09-04T19:40:29', 'delivered_at': '2022-09-04T19:40:29'}, {'product_id': 2408, 'ordered_quantity': 2, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 86.5, 'expected_delivery_at': '2022-09-02T17:19:55', 'delivered_at': '2022-09-02T17:19:55'}]}, {'order_id': 1033, 'address_id': 70, 'payment_card_id': 157, 'name': '2 harps, 1 smart thermostat, 1 picture frame', 'tax': 720.9, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2022-08-26T03:25:45', 'address_text': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'payment_card_digits': '5688', 'paid_amount': 7929.9, 'order_items': [{'product_id': 457, 'ordered_quantity': 2, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 3495.0, 'expected_delivery_at': '2022-08-30T19:30:12', 'delivered_at': '2022-08-30T19:30:12'}, {'product_id': 1462, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 189.0, 'expected_delivery_at': '2022-08-30T18:19:57', 'delivered_at': '2022-08-30T18:19:57'}, {'product_id': 1535, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 30.0, 'expected_delivery_at': '2022-09-01T17:12:03', 'delivered_at': '2022-09-01T17:12:03'}]}, {'order_id': 1023, 'address_id': 70, 'payment_card_id': 157, 'name': '2 beach chairs, 2 coffee makers', 'tax': 37.96, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2022-08-22T03:39:08', 'address_text': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'payment_card_digits': '5688', 'paid_amount': 417.56, 'order_items': [{'product_id': 1338, 'ordered_quantity': 2, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 40.8, 'expected_delivery_at': '2022-08-29T19:06:38', 'delivered_at': '2022-08-29T19:06:38'}, {'product_id': 1391, 'ordered_quantity': 2, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 149.0, 'expected_delivery_at': '2022-08-29T19:45:03', 'delivered_at': '2022-08-29T19:45:03'}]}, {'order_id': 1031, 'address_id': 70, 'payment_card_id': 158, 'name': '2 ironing boards, 2 weightlifting gloves', 'tax': 13.98, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2022-07-31T19:26:08', 'address_text': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'payment_card_digits': '9914', 'paid_amount': 153.78, 'order_items': [{'product_id': 36, 'ordered_quantity': 2, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 50.0, 'expected_delivery_at': '2022-08-03T17:45:10', 'delivered_at': '2022-08-03T17:45:10'}, {'product_id': 2118, 'ordered_quantity': 2, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 19.9, 'expected_delivery_at': '2022-08-06T19:54:36', 'delivered_at': '2022-08-06T19:54:36'}]}, {'order_id': 1025, 'address_id': 70, 'payment_card_id': 157, 'name': '1 bathroom scale, 1 laundry hamper, 2 smart thermostats, 1 computer monitor', 'tax': 149.3, 'delivery_fee': 0.0, 'gift_wrap_fee': 5.0, 'discount': 0.0, 'created_at': '2022-07-28T11:00:16', 'address_text': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'payment_card_digits': '5688', 'paid_amount': 1647.3, 'order_items': [{'product_id': 741, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 35.0, 'expected_delivery_at': '2022-07-29T18:35:21', 'delivered_at': '2022-07-29T18:35:21'}, {'product_id': 1242, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 1, 'price': 60.0, 'expected_delivery_at': '2022-07-29T17:31:54', 'delivered_at': '2022-07-29T17:31:54'}, {'product_id': 1460, 'ordered_quantity': 2, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 249.0, 'expected_delivery_at': '2022-08-03T18:13:08', 'delivered_at': '2022-08-03T18:13:08'}, {'product_id': 2635, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 900.0, 'expected_delivery_at': '2022-08-04T19:04:53', 'delivered_at': '2022-08-04T19:04:53'}]}, {'order_id': 1030, 'address_id': 70, 'payment_card_id': 157, 'name': '2 umbrellas, 1 dining chair', 'tax': 13.9, 'delivery_fee': 0.0, 'gift_wrap_fee': 10.0, 'discount': 0.0, 'created_at': '2022-07-17T11:58:45', 'address_text': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'payment_card_digits': '5688', 'paid_amount': 162.9, 'order_items': [{'product_id': 1280, 'ordered_quantity': 2, 'returned_quantity': 0, 'gift_wrap_quantity': 2, 'price': 30.0, 'expected_delivery_at': '2022-07-23T18:54:04', 'delivered_at': '2022-07-23T18:54:04'}, {'product_id': 2153, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 79.0, 'expected_delivery_at': '2022-07-20T18:57:54', 'delivered_at': '2022-07-20T18:57:54'}]}, {'order_id': 1024, 'address_id': 70, 'payment_card_id': 158, 'name': '2 sunscreens, 1 coffee table, 2 swimsuits', 'tax': 37.4, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2022-06-11T16:51:20', 'address_text': '716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529', 'payment_card_digits': '9914', 'paid_amount': 411.4, 'order_items': [{'product_id': 679, 'ordered_quantity': 2, 'returned_quantity': 1, 'gift_wrap_quantity': 0, 'price': 7.0, 'expected_delivery_at': '2022-06-17T19:42:32', 'delivered_at': '2022-06-17T19:42:32'}, {'product_id': 1320, 'ordered_quantity': 1, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 300.0, 'expected_delivery_at': '2022-06-15T18:45:38', 'delivered_at': '2022-06-15T18:45:38'}, {'product_id': 2687, 'ordered_quantity': 2, 'returned_quantity': 0, 'gift_wrap_quantity': 0, 'price': 30.0, 'expected_delivery_at': '2022-06-13T18:37:45', 'delivered_at': '2022-06-13T18:37:45'}]}]
```


### Environment Interaction 9
----------------------------------------------------------------------------
```python
trusted_sellers = set()
for order in orders:
    for item in order['order_items']:
        # Assuming product_id can be used to get seller information
        product_info = apis.amazon.show_product(product_id=item['product_id'])
        seller_id = product_info['seller_id']
        trusted_sellers.add(seller_id)
print('Trusted sellers:', trusted_sellers)
```

```
Trusted sellers: {256, 3, 4, 131, 6, 7, 11, 268, 139, 14, 15, 145, 21, 285, 33, 162, 163, 36, 168, 42, 298, 44, 170, 302, 179, 310, 184, 57, 187, 190, 62, 64, 319, 70, 71, 198, 201, 74, 202, 78, 79, 81, 211, 87, 216, 102, 104, 109, 240, 120, 126}
```


### Environment Interaction 10
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='amazon'))
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='search_products'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_verification_code",
  "description": "Send account verification code to your email address."
 },
 {
  "name": "verify_account",
  "description": "Verify your account using the verification code sent to your email address."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "show_product",
  "description": "Show product information based on its ID."
 },
 {
  "name": "search_sellers",
  "description": "Search for sellers with a query."
 },
 {
  "name": "show_seller",
  "description": "Show a detailed information about the seller."
 },
 {
  "name": "search_product_types",
  "description": "Search product types present in the database."
 },
 {
  "name": "show_product_feature_choices",
  "description": "Show the choices of colors, relative sizes and sellers aggregated over all products of the given product type. Because it's an aggregation, the choices may not be available for all products. If product type is not passed, it will return the choices for all products in the database."
 },
 {
  "name": "search_products",
  "description": "Search for products with a query and various filtering criteria."
 },
 {
  "name": "show_cart",
  "description": "show your cart."
 },
 {
  "name": "clear_cart",
  "description": "Clear your cart."
 },
 {
  "name": "add_product_to_cart",
  "description": "Add product by id and quantities to your cart."
 },
 {
  "name": "delete_product_from_cart",
  "description": "Remove a product from your cart."
 },
 {
  "name": "update_product_quantity_in_cart",
  "description": "Update product quantity in the user cart."
 },
 {
  "name": "apply_promo_code_to_cart",
  "description": "Apply a promo code to your cart."
 },
 {
  "name": "remove_promo_code_from_cart",
  "description": "Remove a promo code from your cart."
 },
 {
  "name": "show_wish_list",
  "description": "Get list of products in your wishlist."
 },
 {
  "name": "clear_wish_list",
  "description": "Clear wish list."
 },
 {
  "name": "add_product_to_wish_list",
  "description": "Add product by id and quantities to your wish list."
 },
 {
  "name": "delete_product_from_wish_list",
  "description": "Remove product from the user wish list."
 },
 {
  "name": "update_product_quantity_in_wish_list",
  "description": "Update product quantity in the user wish_list."
 },
 {
  "name": "move_product_from_cart_to_wish_list",
  "description": "Move product from the cart to the wish list."
 },
 {
  "name": "move_product_from_wish_list_to_cart",
  "description": "Move product from the wish list to the cart."
 },
 {
  "name": "add_gift_wrapping_to_product",
  "description": "Add gift wrapping to a product in your cart. If the product is already set to be gift wrapped, its quantity will be updated."
 },
 {
  "name": "remove_gift_wrapping_from_product",
  "description": "Remove gift wrapping from a product in your cart."
 },
 {
  "name": "show_orders",
  "description": "Show or search your past orders"
 },
 {
  "name": "place_order",
  "description": "Place an order for all the items in your cart."
 },
 {
  "name": "show_order",
  "description": "Get details of a past order."
 },
 {
  "name": "download_order_receipt",
  "description": "Download the receipt of a past order."
 },
 {
  "name": "show_payment_cards",
  "description": "Get a list of your payment_cards."
 },
 {
  "name": "add_payment_card",
  "description": "Add a new payment card."
 },
 {
  "name": "show_payment_card",
  "description": "Get details of a payment card."
 },
 {
  "name": "delete_payment_card",
  "description": "Delete payment card information."
 },
 {
  "name": "update_payment_card",
  "description": "Update payment card information."
 },
 {
  "name": "show_addresses",
  "description": "Get a list of your addresses."
 },
 {
  "name": "add_address",
  "description": "Add a new address."
 },
 {
  "name": "delete_address",
  "description": "Delete address information."
 },
 {
  "name": "update_address",
  "description": "Update address information."
 },
 {
  "name": "show_product_reviews",
  "description": "Get a list of product reviews."
 },
 {
  "name": "write_product_review",
  "description": "Write a product review."
 },
 {
  "name": "delete_product_review",
  "description": "Delete a product review."
 },
 {
  "name": "update_product_review",
  "description": "Update a product review."
 },
 {
  "name": "show_product_questions",
  "description": "Get a list of product questions."
 },
 {
  "name": "write_product_question",
  "description": "Post a question about a product."
 },
 {
  "name": "show_product_question_answers",
  "description": "Get a list of answers to a product question."
 },
 {
  "name": "write_product_question_answer",
  "description": "Write a answer to a product question."
 },
 {
  "name": "delete_product_question",
  "description": "Delete a product question."
 },
 {
  "name": "update_product_question",
  "description": "Update a product question."
 },
 {
  "name": "delete_product_question_answer",
  "description": "Delete a answer to a product question."
 },
 {
  "name": "update_product_question_answer",
  "description": "Update answer to a product question."
 },
 {
  "name": "show_returns",
  "description": "Get a list of your product returns."
 },
 {
  "name": "initiate_return",
  "description": "Initiate a product return."
 },
 {
  "name": "show_return",
  "description": "Show product return status."
 },
 {
  "name": "show_return_deliverers",
  "description": "Get a list of product return deliverers."
 },
 {
  "name": "show_prime_plans",
  "description": "Show information about prime plans available. Delivery fee is waived for prime members."
 },
 {
  "name": "show_prime_subscriptions",
  "description": "Show your prime subscription history."
 },
 {
  "name": "subscribe_prime",
  "description": "Subscribe to prime membership."
 },
 {
  "name": "download_prime_subscription_receipt",
  "description": "Download the receipt for a prime subscription."
 }
]
{
 "app_name": "amazon",
 "api_name": "search_products",
 "path": "/products",
 "method": "GET",
 "description": "Search for products with a query and various filtering criteria.",
 "parameters": [
  {
   "name": "query",
   "type": "string",
   "required": false,
   "description": "The search query string.",
   "default": "",
   "constraints": []
  },
  {
   "name": "product_type",
   "type": "string",
   "required": false,
   "description": "The type of product to search for.",
   "default": null,
   "constraints": []
  },
  {
   "name": "color",
   "type": "string",
   "required": false,
   "description": "The color of product to search for.",
   "default": null,
   "constraints": []
  },
  {
   "name": "relative_size",
   "type": "string",
   "required": false,
   "description": "The relative size of product to search for.",
   "default": null,
   "constraints": [
    "value in ['extra-small', 'small', 'medium', 'large', 'extra-large']"
   ]
  },
  {
   "name": "min_price",
   "type": "number",
   "required": false,
   "description": "The minimum price for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "max_price",
   "type": "number",
   "required": false,
   "description": "The maximum price for search results.",
   "default": 9223372036854775807,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "min_product_rating",
   "type": "number",
   "required": false,
   "description": "The minimum product rating for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "max_product_rating",
   "type": "number",
   "required": false,
   "description": "The maximum product rating for search results.",
   "default": 5,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "min_seller_rating",
   "type": "number",
   "required": false,
   "description": "The minimum seller rating for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "max_seller_rating",
   "type": "number",
   "required": false,
   "description": "The maximum seller rating for search results.",
   "default": 5,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "seller_id",
   "type": "integer",
   "required": false,
   "description": "ID of the seller to search for.",
   "default": null,
   "constraints": []
  },
  {
   "name": "page_index",
   "type": "integer",
   "required": false,
   "description": "The index of the page to return.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "page_limit",
   "type": "integer",
   "required": false,
   "description": "The maximum number of results to return per page.",
   "default": 5,
   "constraints": [
    "value >= 1.0, <= 20.0"
   ]
  },
  {
   "name": "sort_by",
   "type": "string",
   "required": false,
   "description": "The attribute to sort the products by prefixed with +/- to reflect ascending/descending. Valid attributes: rating, price and delivery_days. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": [
   {
    "product_id": 1,
    "seller_id": 1,
    "product_type": "string",
    "name": "string",
    "description": "string",
    "price": 0.0,
    "delivery_days": 1.0,
    "inventory_quantity": 0.0,
    "weight": 0.0,
    "length": 0.0,
    "width": 0.0,
    "height": 0.0,
    "color": "string",
    "relative_size": "extra-small",
    "rating": 0.0,
    "num_product_reviews": 1,
    "num_product_questions": 1,
    "variations": [
     {
      "product_id": 1,
      "relative_size": "extra-small",
      "color": "string"
     }
    ]
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 11
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='search_products'))
```

```
{
 "app_name": "amazon",
 "api_name": "search_products",
 "path": "/products",
 "method": "GET",
 "description": "Search for products with a query and various filtering criteria.",
 "parameters": [
  {
   "name": "query",
   "type": "string",
   "required": false,
   "description": "The search query string.",
   "default": "",
   "constraints": []
  },
  {
   "name": "product_type",
   "type": "string",
   "required": false,
   "description": "The type of product to search for.",
   "default": null,
   "constraints": []
  },
  {
   "name": "color",
   "type": "string",
   "required": false,
   "description": "The color of product to search for.",
   "default": null,
   "constraints": []
  },
  {
   "name": "relative_size",
   "type": "string",
   "required": false,
   "description": "The relative size of product to search for.",
   "default": null,
   "constraints": [
    "value in ['extra-small', 'small', 'medium', 'large', 'extra-large']"
   ]
  },
  {
   "name": "min_price",
   "type": "number",
   "required": false,
   "description": "The minimum price for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "max_price",
   "type": "number",
   "required": false,
   "description": "The maximum price for search results.",
   "default": 9223372036854775807,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "min_product_rating",
   "type": "number",
   "required": false,
   "description": "The minimum product rating for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "max_product_rating",
   "type": "number",
   "required": false,
   "description": "The maximum product rating for search results.",
   "default": 5,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "min_seller_rating",
   "type": "number",
   "required": false,
   "description": "The minimum seller rating for search results.",
   "default": 0,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "max_seller_rating",
   "type": "number",
   "required": false,
   "description": "The maximum seller rating for search results.",
   "default": 5,
   "constraints": [
    "value >= 0.0, <= 5.0"
   ]
  },
  {
   "name": "seller_id",
   "type": "integer",
   "required": false,
   "description": "ID of the seller to search for.",
   "default": null,
   "constraints": []
  },
  {
   "name": "page_index",
   "type": "integer",
   "required": false,
   "description": "The index of the page to return.",
   "default": 0,
   "constraints": [
    "value >= 0.0"
   ]
  },
  {
   "name": "page_limit",
   "type": "integer",
   "required": false,
   "description": "The maximum number of results to return per page.",
   "default": 5,
   "constraints": [
    "value >= 1.0, <= 20.0"
   ]
  },
  {
   "name": "sort_by",
   "type": "string",
   "required": false,
   "description": "The attribute to sort the products by prefixed with +/- to reflect ascending/descending. Valid attributes: rating, price and delivery_days. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": [
   {
    "product_id": 1,
    "seller_id": 1,
    "product_type": "string",
    "name": "string",
    "description": "string",
    "price": 0.0,
    "delivery_days": 1.0,
    "inventory_quantity": 0.0,
    "weight": 0.0,
    "length": 0.0,
    "width": 0.0,
    "height": 0.0,
    "color": "string",
    "relative_size": "extra-small",
    "rating": 0.0,
    "num_product_reviews": 1,
    "num_product_questions": 1,
    "variations": [
     {
      "product_id": 1,
      "relative_size": "extra-small",
      "color": "string"
     }
    ]
   }
  ],
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 12
----------------------------------------------------------------------------
```python
watches = []
page_index = 0
while True:
    response = apis.amazon.search_products(query='watch', max_price=110, page_index=page_index)
    watches.extend(response)
    if len(response) < 20:  # assuming default page limit is 20
        break
    page_index += 1
print('Watches:', watches)
```

```
Watches: [{'product_id': 1403, 'seller_id': 183, 'product_type': 'watch', 'name': "Casio Baby-G Women's Watch", 'description': 'Stylish and sporty watch for active women', 'price': 80.0, 'delivery_days': 7, 'inventory_quantity': 6, 'weight': 0.06, 'length': 1.8, 'width': 1.8, 'height': 0.6, 'color': 'pink', 'relative_size': 'small', 'rating': 5.0, 'num_product_reviews': 3, 'num_product_questions': 4, 'variations': []}, {'product_id': 1406, 'seller_id': 184, 'product_type': 'watch', 'name': "Fossil Men's The Minimalist Quartz Watch", 'description': 'Simple and stylish quartz watch for men', 'price': 109.0, 'delivery_days': 2, 'inventory_quantity': 5, 'weight': 0.2, 'length': 2.0, 'width': 2.0, 'height': 0.4, 'color': 'brown', 'relative_size': 'medium', 'rating': 3.8, 'num_product_reviews': 6, 'num_product_questions': 4, 'variations': []}, {'product_id': 1407, 'seller_id': 184, 'product_type': 'watch', 'name': "Fossil Women's Riley Multifunction Glitz Quartz Watch", 'description': 'Elegant and sparkling quartz watch for women', 'price': 105.0, 'delivery_days': 2, 'inventory_quantity': 28, 'weight': 0.2, 'length': 2.0, 'width': 2.0, 'height': 0.4, 'color': 'silver', 'relative_size': 'medium', 'rating': 3.9, 'num_product_reviews': 7, 'num_product_questions': 4, 'variations': []}, {'product_id': 2036, 'seller_id': 6, 'product_type': 'metronome', 'name': 'TAMA Rhythm Watch RW200', 'description': 'Compact metronome for precise timing in music', 'price': 45.0, 'delivery_days': 4, 'inventory_quantity': 2, 'weight': 0.12, 'length': 3.5, 'width': 2.0, 'height': 0.75, 'color': 'silver', 'relative_size': 'small', 'rating': 4.0, 'num_product_reviews': 6, 'num_product_questions': 4, 'variations': []}, {'product_id': 1, 'seller_id': 1, 'product_type': 'hiking socks', 'name': 'Smartwool Hike Medium Crew Socks', 'description': 'Medium cushioned hiking socks with merino wool blend.', 'price': 19.9, 'delivery_days': 4, 'inventory_quantity': 28, 'weight': 0.11, 'length': 11.5, 'width': 4.5, 'height': 1.0, 'color': 'taupe', 'relative_size': 'medium', 'rating': 3.3, 'num_product_reviews': 9, 'num_product_questions': 4, 'variations': []}]
```


### Environment Interaction 13
----------------------------------------------------------------------------
```python
trusted_sellers = {256, 3, 4, 131, 6, 7, 11, 268, 139, 14, 15, 145, 21, 285, 33, 162, 163, 36, 168, 42, 298, 44, 170, 302, 179, 310, 184, 57, 187, 190, 62, 64, 319, 70, 71, 198, 201, 74, 202, 78, 79, 81, 211, 87, 216, 102, 104, 109, 240, 120, 126}
filtered_watches = [watch for watch in watches if watch['seller_id'] in trusted_sellers and watch['product_type'] == 'watch']
print('Filtered watches:', filtered_watches)
```

```
Filtered watches: [{'product_id': 1406, 'seller_id': 184, 'product_type': 'watch', 'name': "Fossil Men's The Minimalist Quartz Watch", 'description': 'Simple and stylish quartz watch for men', 'price': 109.0, 'delivery_days': 2, 'inventory_quantity': 5, 'weight': 0.2, 'length': 2.0, 'width': 2.0, 'height': 0.4, 'color': 'brown', 'relative_size': 'medium', 'rating': 3.8, 'num_product_reviews': 6, 'num_product_questions': 4, 'variations': []}, {'product_id': 1407, 'seller_id': 184, 'product_type': 'watch', 'name': "Fossil Women's Riley Multifunction Glitz Quartz Watch", 'description': 'Elegant and sparkling quartz watch for women', 'price': 105.0, 'delivery_days': 2, 'inventory_quantity': 28, 'weight': 0.2, 'length': 2.0, 'width': 2.0, 'height': 0.4, 'color': 'silver', 'relative_size': 'medium', 'rating': 3.9, 'num_product_reviews': 7, 'num_product_questions': 4, 'variations': []}]
```


### Environment Interaction 14
----------------------------------------------------------------------------
```python
selected_watch = filtered_watches[0]  # select the first watch
print('Selected watch:', selected_watch)
apis.amazon.add_product_to_cart(product_id=selected_watch['product_id'], quantity=1)
```

```
Execution failed. Traceback:
  File "<python-input>", line 3, in <module>
    apis.amazon.add_product_to_cart(product_id=selected_watch['product_id'], quantity=1)
Exception: Response status code is 401:
{"message":"You are either not authorized to access this amazon API endpoint or your access token is missing, invalid or expired."}
```


### Environment Interaction 15
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='login'))
amazon_password = [p for p in apis.supervisor.show_account_passwords() if p['account_name'] == 'amazon'][0]['password']
access_token = apis.amazon.login(username='chelsea-burch@gmail.com', password=amazon_password)['access_token']
print('New Amazon access token:', access_token)
```

```
{
 "app_name": "amazon",
 "api_name": "login",
 "path": "/auth/token",
 "method": "POST",
 "description": "Login to your account.",
 "parameters": [
  {
   "name": "username",
   "type": "string",
   "required": true,
   "description": "Your account email.",
   "default": null,
   "constraints": []
  },
  {
   "name": "password",
   "type": "string",
   "required": true,
   "description": "Your account password.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "access_token": "string",
   "token_type": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
New Amazon access token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbWF6b24rY2hlbHNlYS1idXJjaEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTI3NDF9.7lU6bDdlaAYMxMMpJ2m3vKAoVVx6GOOjorBLKWhu9Jg
```


### Environment Interaction 16
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='add_product_to_cart'))
```

```
{
 "app_name": "amazon",
 "api_name": "add_product_to_cart",
 "path": "/cart/{product_id}",
 "method": "POST",
 "description": "Add product by id and quantities to your cart.",
 "parameters": [
  {
   "name": "product_id",
   "type": "integer",
   "required": true,
   "description": "ID of the product to be added to the cart.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from amazon app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "quantity",
   "type": "integer",
   "required": false,
   "description": "The quantity of the product to be added to the cart.",
   "default": 1,
   "constraints": [
    "value >= 1.0"
   ]
  },
  {
   "name": "clear_cart_first",
   "type": "boolean",
   "required": false,
   "description": "If true, the cart will be cleared before adding the product to the cart.",
   "default": false,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 17
----------------------------------------------------------------------------
```python
amazon_password = [p for p in apis.supervisor.show_account_passwords() if p['account_name'] == 'amazon'][0]['password']
access_token = apis.amazon.login(username='chelsea-burch@gmail.com', password=amazon_password)['access_token']
apis.amazon.add_product_to_cart(product_id=1406, quantity=1, access_token=access_token)
print(apis.api_docs.show_api_descriptions(app_name='amazon'))
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='place_order'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_verification_code",
  "description": "Send account verification code to your email address."
 },
 {
  "name": "verify_account",
  "description": "Verify your account using the verification code sent to your email address."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "show_product",
  "description": "Show product information based on its ID."
 },
 {
  "name": "search_sellers",
  "description": "Search for sellers with a query."
 },
 {
  "name": "show_seller",
  "description": "Show a detailed information about the seller."
 },
 {
  "name": "search_product_types",
  "description": "Search product types present in the database."
 },
 {
  "name": "show_product_feature_choices",
  "description": "Show the choices of colors, relative sizes and sellers aggregated over all products of the given product type. Because it's an aggregation, the choices may not be available for all products. If product type is not passed, it will return the choices for all products in the database."
 },
 {
  "name": "search_products",
  "description": "Search for products with a query and various filtering criteria."
 },
 {
  "name": "show_cart",
  "description": "show your cart."
 },
 {
  "name": "clear_cart",
  "description": "Clear your cart."
 },
 {
  "name": "add_product_to_cart",
  "description": "Add product by id and quantities to your cart."
 },
 {
  "name": "delete_product_from_cart",
  "description": "Remove a product from your cart."
 },
 {
  "name": "update_product_quantity_in_cart",
  "description": "Update product quantity in the user cart."
 },
 {
  "name": "apply_promo_code_to_cart",
  "description": "Apply a promo code to your cart."
 },
 {
  "name": "remove_promo_code_from_cart",
  "description": "Remove a promo code from your cart."
 },
 {
  "name": "show_wish_list",
  "description": "Get list of products in your wishlist."
 },
 {
  "name": "clear_wish_list",
  "description": "Clear wish list."
 },
 {
  "name": "add_product_to_wish_list",
  "description": "Add product by id and quantities to your wish list."
 },
 {
  "name": "delete_product_from_wish_list",
  "description": "Remove product from the user wish list."
 },
 {
  "name": "update_product_quantity_in_wish_list",
  "description": "Update product quantity in the user wish_list."
 },
 {
  "name": "move_product_from_cart_to_wish_list",
  "description": "Move product from the cart to the wish list."
 },
 {
  "name": "move_product_from_wish_list_to_cart",
  "description": "Move product from the wish list to the cart."
 },
 {
  "name": "add_gift_wrapping_to_product",
  "description": "Add gift wrapping to a product in your cart. If the product is already set to be gift wrapped, its quantity will be updated."
 },
 {
  "name": "remove_gift_wrapping_from_product",
  "description": "Remove gift wrapping from a product in your cart."
 },
 {
  "name": "show_orders",
  "description": "Show or search your past orders"
 },
 {
  "name": "place_order",
  "description": "Place an order for all the items in your cart."
 },
 {
  "name": "show_order",
  "description": "Get details of a past order."
 },
 {
  "name": "download_order_receipt",
  "description": "Download the receipt of a past order."
 },
 {
  "name": "show_payment_cards",
  "description": "Get a list of your payment_cards."
 },
 {
  "name": "add_payment_card",
  "description": "Add a new payment card."
 },
 {
  "name": "show_payment_card",
  "description": "Get details of a payment card."
 },
 {
  "name": "delete_payment_card",
  "description": "Delete payment card information."
 },
 {
  "name": "update_payment_card",
  "description": "Update payment card information."
 },
 {
  "name": "show_addresses",
  "description": "Get a list of your addresses."
 },
 {
  "name": "add_address",
  "description": "Add a new address."
 },
 {
  "name": "delete_address",
  "description": "Delete address information."
 },
 {
  "name": "update_address",
  "description": "Update address information."
 },
 {
  "name": "show_product_reviews",
  "description": "Get a list of product reviews."
 },
 {
  "name": "write_product_review",
  "description": "Write a product review."
 },
 {
  "name": "delete_product_review",
  "description": "Delete a product review."
 },
 {
  "name": "update_product_review",
  "description": "Update a product review."
 },
 {
  "name": "show_product_questions",
  "description": "Get a list of product questions."
 },
 {
  "name": "write_product_question",
  "description": "Post a question about a product."
 },
 {
  "name": "show_product_question_answers",
  "description": "Get a list of answers to a product question."
 },
 {
  "name": "write_product_question_answer",
  "description": "Write a answer to a product question."
 },
 {
  "name": "delete_product_question",
  "description": "Delete a product question."
 },
 {
  "name": "update_product_question",
  "description": "Update a product question."
 },
 {
  "name": "delete_product_question_answer",
  "description": "Delete a answer to a product question."
 },
 {
  "name": "update_product_question_answer",
  "description": "Update answer to a product question."
 },
 {
  "name": "show_returns",
  "description": "Get a list of your product returns."
 },
 {
  "name": "initiate_return",
  "description": "Initiate a product return."
 },
 {
  "name": "show_return",
  "description": "Show product return status."
 },
 {
  "name": "show_return_deliverers",
  "description": "Get a list of product return deliverers."
 },
 {
  "name": "show_prime_plans",
  "description": "Show information about prime plans available. Delivery fee is waived for prime members."
 },
 {
  "name": "show_prime_subscriptions",
  "description": "Show your prime subscription history."
 },
 {
  "name": "subscribe_prime",
  "description": "Subscribe to prime membership."
 },
 {
  "name": "download_prime_subscription_receipt",
  "description": "Download the receipt for a prime subscription."
 }
]
{
 "app_name": "amazon",
 "api_name": "place_order",
 "path": "/orders",
 "method": "POST",
 "description": "Place an order for all the items in your cart.",
 "parameters": [
  {
   "name": "payment_card_id",
   "type": "integer",
   "required": true,
   "description": "ID of the payment card to use for this order.",
   "default": null,
   "constraints": []
  },
  {
   "name": "address_id",
   "type": "integer",
   "required": true,
   "description": "ID of the address used for shipping this order.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from amazon app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string",
   "order_id": 1
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 18
----------------------------------------------------------------------------
```python
account_info = apis.amazon.show_account(access_token=access_token)
address_id = account_info['address_id']
payment_method_id = account_info['payment_method_id']
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='place_order'))
apis.amazon.place_order(address_id=address_id, payment_method_id=payment_method_id, access_token=access_token)
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    address_id = account_info['address_id']
                 ~~~~~~~~~~~~^^^^^^^^^^^^^^
KeyError: 'address_id'
```


### Environment Interaction 19
----------------------------------------------------------------------------
```python
account_info = apis.amazon.show_account(access_token=access_token)
print(account_info)
```

```
{
 "first_name": "Chelsea",
 "last_name": "Burch",
 "email": "chelsea-burch@gmail.com",
 "registered_at": "2022-06-10T13:07:41",
 "last_logged_in": "2022-06-10T13:07:41",
 "verified": true,
 "is_prime": true
}
```


### Environment Interaction 20
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='amazon'))
print(apis.api_docs.search_api_docs(query='address'))
print(apis.api_docs.search_api_docs(query='payment'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_verification_code",
  "description": "Send account verification code to your email address."
 },
 {
  "name": "verify_account",
  "description": "Verify your account using the verification code sent to your email address."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "show_product",
  "description": "Show product information based on its ID."
 },
 {
  "name": "search_sellers",
  "description": "Search for sellers with a query."
 },
 {
  "name": "show_seller",
  "description": "Show a detailed information about the seller."
 },
 {
  "name": "search_product_types",
  "description": "Search product types present in the database."
 },
 {
  "name": "show_product_feature_choices",
  "description": "Show the choices of colors, relative sizes and sellers aggregated over all products of the given product type. Because it's an aggregation, the choices may not be available for all products. If product type is not passed, it will return the choices for all products in the database."
 },
 {
  "name": "search_products",
  "description": "Search for products with a query and various filtering criteria."
 },
 {
  "name": "show_cart",
  "description": "show your cart."
 },
 {
  "name": "clear_cart",
  "description": "Clear your cart."
 },
 {
  "name": "add_product_to_cart",
  "description": "Add product by id and quantities to your cart."
 },
 {
  "name": "delete_product_from_cart",
  "description": "Remove a product from your cart."
 },
 {
  "name": "update_product_quantity_in_cart",
  "description": "Update product quantity in the user cart."
 },
 {
  "name": "apply_promo_code_to_cart",
  "description": "Apply a promo code to your cart."
 },
 {
  "name": "remove_promo_code_from_cart",
  "description": "Remove a promo code from your cart."
 },
 {
  "name": "show_wish_list",
  "description": "Get list of products in your wishlist."
 },
 {
  "name": "clear_wish_list",
  "description": "Clear wish list."
 },
 {
  "name": "add_product_to_wish_list",
  "description": "Add product by id and quantities to your wish list."
 },
 {
  "name": "delete_product_from_wish_list",
  "description": "Remove product from the user wish list."
 },
 {
  "name": "update_product_quantity_in_wish_list",
  "description": "Update product quantity in the user wish_list."
 },
 {
  "name": "move_product_from_cart_to_wish_list",
  "description": "Move product from the cart to the wish list."
 },
 {
  "name": "move_product_from_wish_list_to_cart",
  "description": "Move product from the wish list to the cart."
 },
 {
  "name": "add_gift_wrapping_to_product",
  "description": "Add gift wrapping to a product in your cart. If the product is already set to be gift wrapped, its quantity will be updated."
 },
 {
  "name": "remove_gift_wrapping_from_product",
  "description": "Remove gift wrapping from a product in your cart."
 },
 {
  "name": "show_orders",
  "description": "Show or search your past orders"
 },
 {
  "name": "place_order",
  "description": "Place an order for all the items in your cart."
 },
 {
  "name": "show_order",
  "description": "Get details of a past order."
 },
 {
  "name": "download_order_receipt",
  "description": "Download the receipt of a past order."
 },
 {
  "name": "show_payment_cards",
  "description": "Get a list of your payment_cards."
 },
 {
  "name": "add_payment_card",
  "description": "Add a new payment card."
 },
 {
  "name": "show_payment_card",
  "description": "Get details of a payment card."
 },
 {
  "name": "delete_payment_card",
  "description": "Delete payment card information."
 },
 {
  "name": "update_payment_card",
  "description": "Update payment card information."
 },
 {
  "name": "show_addresses",
  "description": "Get a list of your addresses."
 },
 {
  "name": "add_address",
  "description": "Add a new address."
 },
 {
  "name": "delete_address",
  "description": "Delete address information."
 },
 {
  "name": "update_address",
  "description": "Update address information."
 },
 {
  "name": "show_product_reviews",
  "description": "Get a list of product reviews."
 },
 {
  "name": "write_product_review",
  "description": "Write a product review."
 },
 {
  "name": "delete_product_review",
  "description": "Delete a product review."
 },
 {
  "name": "update_product_review",
  "description": "Update a product review."
 },
 {
  "name": "show_product_questions",
  "description": "Get a list of product questions."
 },
 {
  "name": "write_product_question",
  "description": "Post a question about a product."
 },
 {
  "name": "show_product_question_answers",
  "description": "Get a list of answers to a product question."
 },
 {
  "name": "write_product_question_answer",
  "description": "Write a answer to a product question."
 },
 {
  "name": "delete_product_question",
  "description": "Delete a product question."
 },
 {
  "name": "update_product_question",
  "description": "Update a product question."
 },
 {
  "name": "delete_product_question_answer",
  "description": "Delete a answer to a product question."
 },
 {
  "name": "update_product_question_answer",
  "description": "Update answer to a product question."
 },
 {
  "name": "show_returns",
  "description": "Get a list of your product returns."
 },
 {
  "name": "initiate_return",
  "description": "Initiate a product return."
 },
 {
  "name": "show_return",
  "description": "Show product return status."
 },
 {
  "name": "show_return_deliverers",
  "description": "Get a list of product return deliverers."
 },
 {
  "name": "show_prime_plans",
  "description": "Show information about prime plans available. Delivery fee is waived for prime members."
 },
 {
  "name": "show_prime_subscriptions",
  "description": "Show your prime subscription history."
 },
 {
  "name": "subscribe_prime",
  "description": "Subscribe to prime membership."
 },
 {
  "name": "download_prime_subscription_receipt",
  "description": "Download the receipt for a prime subscription."
 }
]
[
 {
  "app_name": "amazon",
  "api_name": "delete_address",
  "path": "/addresses/{address_id}",
  "method": "DELETE",
  "description": "Delete address information.",
  "parameters": [
   {
    "name": "address_id",
    "type": "integer",
    "required": true,
    "description": "ID of the address to be deleted.",
    "default": null,
    "constraints": []
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "amazon",
  "api_name": "update_address",
  "path": "/addresses/{address_id}",
  "method": "PATCH",
  "description": "Update address information.",
  "parameters": [
   {
    "name": "address_id",
    "type": "integer",
    "required": true,
    "description": "ID of the address to update",
    "default": null,
    "constraints": []
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   },
   {
    "name": "name",
    "type": "string",
    "required": false,
    "description": "New name for the address",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "street_address",
    "type": "string",
    "required": false,
    "description": "New street address line.",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "city",
    "type": "string",
    "required": false,
    "description": "New city name for the address",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "state",
    "type": "string",
    "required": false,
    "description": "New state name for the address",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "country",
    "type": "string",
    "required": false,
    "description": "New country name for the address",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "zip_code",
    "type": "integer",
    "required": false,
    "description": "New ZIP code for the address",
    "default": null,
    "constraints": [
     "value >= 10000.0, <= 99999.0"
    ]
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "amazon",
  "api_name": "add_address",
  "path": "/addresses",
  "method": "POST",
  "description": "Add a new address.",
  "parameters": [
   {
    "name": "name",
    "type": "string",
    "required": true,
    "description": "Name of the address, for example 'Home' or 'Work'.",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "street_address",
    "type": "string",
    "required": true,
    "description": "Street address line.",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "city",
    "type": "string",
    "required": true,
    "description": "Name of the city.",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "state",
    "type": "string",
    "required": true,
    "description": "Name of the state.",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "country",
    "type": "string",
    "required": true,
    "description": "Name of the country.",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "zip_code",
    "type": "integer",
    "required": true,
    "description": "5-digit zip code of the address.",
    "default": null,
    "constraints": [
     "value >= 10000.0, < 100000.0"
    ]
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string",
    "address_id": 1
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "supervisor",
  "api_name": "show_addresses",
  "path": "/addresses",
  "method": "GET",
  "description": "Show your supervisor's addresses.",
  "parameters": [],
  "response_schemas": {
   "success": [
    {
     "name": "Home",
     "street_address": "string",
     "city": "string",
     "state": "string",
     "country": "string",
     "zip_code": 10000.0
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "amazon",
  "api_name": "show_addresses",
  "path": "/addresses",
  "method": "GET",
  "description": "Get a list of your addresses.",
  "parameters": [
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "address_id": 1,
     "name": "string",
     "street_address": "string",
     "city": "string",
     "state": "string",
     "country": "string",
     "zip_code": 10000.0
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 }
]
[
 {
  "app_name": "splitwise",
  "api_name": "update_payment",
  "path": "/payments/{payment_id}",
  "method": "PATCH",
  "description": "Update payment information.",
  "parameters": [
   {
    "name": "payment_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the payment.",
    "default": null,
    "constraints": []
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from splitwise app login.",
    "default": null,
    "constraints": []
   },
   {
    "name": "amount",
    "type": "number",
    "required": false,
    "description": "The updated amount of the payment.",
    "default": null,
    "constraints": []
   },
   {
    "name": "description",
    "type": "string",
    "required": false,
    "description": "The updated note or description of the payment.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "amazon",
  "api_name": "delete_payment_card",
  "path": "/payment_cards/{payment_card_id}",
  "method": "DELETE",
  "description": "Delete payment card information.",
  "parameters": [
   {
    "name": "payment_card_id",
    "type": "integer",
    "required": true,
    "description": "ID of the payment card to be deleted.",
    "default": null,
    "constraints": []
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "amazon",
  "api_name": "update_payment_card",
  "path": "/payment_cards/{payment_card_id}",
  "method": "PATCH",
  "description": "Update payment card information.",
  "parameters": [
   {
    "name": "payment_card_id",
    "type": "integer",
    "required": true,
    "description": "ID of the payment card to update.",
    "default": null,
    "constraints": []
   },
   {
    "name": "card_name",
    "type": "string",
    "required": true,
    "description": "Name of the payment card to update.",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "delete_payment_card",
  "path": "/payment_cards/{payment_card_id}",
  "method": "DELETE",
  "description": "Delete payment card information.",
  "parameters": [
   {
    "name": "payment_card_id",
    "type": "integer",
    "required": true,
    "description": "ID of the payment card to be deleted.",
    "default": null,
    "constraints": []
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from spotify app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "update_payment_card",
  "path": "/payment_cards/{payment_card_id}",
  "method": "PATCH",
  "description": "Update payment card information.",
  "parameters": [
   {
    "name": "payment_card_id",
    "type": "integer",
    "required": true,
    "description": "ID of the payment card to update.",
    "default": null,
    "constraints": []
   },
   {
    "name": "card_name",
    "type": "string",
    "required": true,
    "description": "Name of the payment card to update.",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from spotify app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 }
]
```


### Environment Interaction 21
----------------------------------------------------------------------------
```python
print(apis.api_docs.search_api_docs(query='show_addresses'))
print(apis.api_docs.search_api_docs(query='show_payment_methods'))
```

```
[
 {
  "app_name": "supervisor",
  "api_name": "show_addresses",
  "path": "/addresses",
  "method": "GET",
  "description": "Show your supervisor's addresses.",
  "parameters": [],
  "response_schemas": {
   "success": [
    {
     "name": "Home",
     "street_address": "string",
     "city": "string",
     "state": "string",
     "country": "string",
     "zip_code": 10000.0
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "amazon",
  "api_name": "show_addresses",
  "path": "/addresses",
  "method": "GET",
  "description": "Get a list of your addresses.",
  "parameters": [
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "address_id": 1,
     "name": "string",
     "street_address": "string",
     "city": "string",
     "state": "string",
     "country": "string",
     "zip_code": 10000.0
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "show_app_descriptions",
  "path": "/app_descriptions",
  "method": "GET",
  "description": "Show descriptions for all apps available.",
  "parameters": [],
  "response_schemas": {
   "success": [
    {
     "name": "string",
     "description": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "show_api_descriptions",
  "path": "/api_descriptions",
  "method": "GET",
  "description": "Show descriptions for all APIs available for a given app.",
  "parameters": [
   {
    "name": "app_name",
    "type": "string",
    "required": true,
    "description": "App name to return API descriptions for.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "name": "string",
     "description": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "show_api_doc",
  "path": "/api_doc",
  "method": "GET",
  "description": "Show detailed API doc.",
  "parameters": [
   {
    "name": "app_name",
    "type": "string",
    "required": true,
    "description": "App name for the API.",
    "default": null,
    "constraints": []
   },
   {
    "name": "api_name",
    "type": "string",
    "required": true,
    "description": "Name of the API.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "app_name": "string",
    "api_name": "string",
    "path": "string",
    "method": "string",
    "description": "string",
    "parameters": [
     {
      "name": "string",
      "type": "string",
      "required": true,
      "description": "string",
      "default": null,
      "constraints": [
       "string"
      ]
     }
    ],
    "response_schemas": {
     "success": [
      {}
     ],
     "failure": [
      {}
     ]
    }
   },
   "failure": {
    "message": "string"
   }
  }
 }
]
[
 {
  "app_name": "api_docs",
  "api_name": "show_app_descriptions",
  "path": "/app_descriptions",
  "method": "GET",
  "description": "Show descriptions for all apps available.",
  "parameters": [],
  "response_schemas": {
   "success": [
    {
     "name": "string",
     "description": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "show_api_descriptions",
  "path": "/api_descriptions",
  "method": "GET",
  "description": "Show descriptions for all APIs available for a given app.",
  "parameters": [
   {
    "name": "app_name",
    "type": "string",
    "required": true,
    "description": "App name to return API descriptions for.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "name": "string",
     "description": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "show_api_doc",
  "path": "/api_doc",
  "method": "GET",
  "description": "Show detailed API doc.",
  "parameters": [
   {
    "name": "app_name",
    "type": "string",
    "required": true,
    "description": "App name for the API.",
    "default": null,
    "constraints": []
   },
   {
    "name": "api_name",
    "type": "string",
    "required": true,
    "description": "Name of the API.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "app_name": "string",
    "api_name": "string",
    "path": "string",
    "method": "string",
    "description": "string",
    "parameters": [
     {
      "name": "string",
      "type": "string",
      "required": true,
      "description": "string",
      "default": null,
      "constraints": [
       "string"
      ]
     }
    ],
    "response_schemas": {
     "success": [
      {}
     ],
     "failure": [
      {}
     ]
    }
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "search_api_docs",
  "path": "/api_docs",
  "method": "GET",
  "description": "Search for relevant API docs.",
  "parameters": [
   {
    "name": "query",
    "type": "string",
    "required": false,
    "description": "The search query string.",
    "default": "",
    "constraints": []
   },
   {
    "name": "page_index",
    "type": "integer",
    "required": false,
    "description": "The index of the page to return.",
    "default": 0,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "page_limit",
    "type": "integer",
    "required": false,
    "description": "The maximum number of results to return per page.",
    "default": 5,
    "constraints": [
     "value >= 1.0, <= 20.0"
    ]
   }
  ],
  "response_schemas": {
   "success": [
    {
     "app_name": "string",
     "api_name": "string",
     "path": "string",
     "method": "string",
     "description": "string",
     "parameters": [
      {
       "name": "string",
       "type": "string",
       "required": true,
       "description": "string",
       "default": null,
       "constraints": [
        "string"
       ]
      }
     ],
     "response_schemas": {
      "success": [
       {}
      ],
      "failure": [
       {}
      ]
     }
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "supervisor",
  "api_name": "show_active_task",
  "path": "/active_task",
  "method": "GET",
  "description": "Show the currently active task assigned to you by the supervisor.",
  "parameters": [],
  "response_schemas": {
   "success": {
    "instruction": "string",
    "status": "string",
    "answer": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 }
]
```


### Environment Interaction 22
----------------------------------------------------------------------------
```python
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbWF6b24rY2hlbHNlYS1idXJjaEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTI3NDF9.7lU6bDdlaAYMxMMpJ2m3vKAoVVx6GOOjorBLKWhu9Jg'
addresses = apis.amazon.show_addresses(access_token=access_token)
print(addresses)
```

```
[
 {
  "address_id": 69,
  "name": "Home",
  "street_address": "46567 Matthew Burg Suite 702",
  "city": "Seattle",
  "state": "Washington",
  "country": "United States",
  "zip_code": 15473
 },
 {
  "address_id": 70,
  "name": "Work",
  "street_address": "716 White Drive Suite 52",
  "city": "Seattle",
  "state": "Washington",
  "country": "United States",
  "zip_code": 47529
 }
]
```


### Environment Interaction 23
----------------------------------------------------------------------------
```python
print(apis.api_docs.search_api_docs(query='show_payment_methods'))
```

```
[
 {
  "app_name": "api_docs",
  "api_name": "show_app_descriptions",
  "path": "/app_descriptions",
  "method": "GET",
  "description": "Show descriptions for all apps available.",
  "parameters": [],
  "response_schemas": {
   "success": [
    {
     "name": "string",
     "description": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "show_api_descriptions",
  "path": "/api_descriptions",
  "method": "GET",
  "description": "Show descriptions for all APIs available for a given app.",
  "parameters": [
   {
    "name": "app_name",
    "type": "string",
    "required": true,
    "description": "App name to return API descriptions for.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "name": "string",
     "description": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "show_api_doc",
  "path": "/api_doc",
  "method": "GET",
  "description": "Show detailed API doc.",
  "parameters": [
   {
    "name": "app_name",
    "type": "string",
    "required": true,
    "description": "App name for the API.",
    "default": null,
    "constraints": []
   },
   {
    "name": "api_name",
    "type": "string",
    "required": true,
    "description": "Name of the API.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "app_name": "string",
    "api_name": "string",
    "path": "string",
    "method": "string",
    "description": "string",
    "parameters": [
     {
      "name": "string",
      "type": "string",
      "required": true,
      "description": "string",
      "default": null,
      "constraints": [
       "string"
      ]
     }
    ],
    "response_schemas": {
     "success": [
      {}
     ],
     "failure": [
      {}
     ]
    }
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "search_api_docs",
  "path": "/api_docs",
  "method": "GET",
  "description": "Search for relevant API docs.",
  "parameters": [
   {
    "name": "query",
    "type": "string",
    "required": false,
    "description": "The search query string.",
    "default": "",
    "constraints": []
   },
   {
    "name": "page_index",
    "type": "integer",
    "required": false,
    "description": "The index of the page to return.",
    "default": 0,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "page_limit",
    "type": "integer",
    "required": false,
    "description": "The maximum number of results to return per page.",
    "default": 5,
    "constraints": [
     "value >= 1.0, <= 20.0"
    ]
   }
  ],
  "response_schemas": {
   "success": [
    {
     "app_name": "string",
     "api_name": "string",
     "path": "string",
     "method": "string",
     "description": "string",
     "parameters": [
      {
       "name": "string",
       "type": "string",
       "required": true,
       "description": "string",
       "default": null,
       "constraints": [
        "string"
       ]
      }
     ],
     "response_schemas": {
      "success": [
       {}
      ],
      "failure": [
       {}
      ]
     }
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "supervisor",
  "api_name": "show_active_task",
  "path": "/active_task",
  "method": "GET",
  "description": "Show the currently active task assigned to you by the supervisor.",
  "parameters": [],
  "response_schemas": {
   "success": {
    "instruction": "string",
    "status": "string",
    "answer": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 }
]
```


### Environment Interaction 24
----------------------------------------------------------------------------
```python
print(apis.api_docs.search_api_docs(query='payment_methods'))
```

```
[
 {
  "app_name": "api_docs",
  "api_name": "show_app_descriptions",
  "path": "/app_descriptions",
  "method": "GET",
  "description": "Show descriptions for all apps available.",
  "parameters": [],
  "response_schemas": {
   "success": [
    {
     "name": "string",
     "description": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "show_api_descriptions",
  "path": "/api_descriptions",
  "method": "GET",
  "description": "Show descriptions for all APIs available for a given app.",
  "parameters": [
   {
    "name": "app_name",
    "type": "string",
    "required": true,
    "description": "App name to return API descriptions for.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "name": "string",
     "description": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "show_api_doc",
  "path": "/api_doc",
  "method": "GET",
  "description": "Show detailed API doc.",
  "parameters": [
   {
    "name": "app_name",
    "type": "string",
    "required": true,
    "description": "App name for the API.",
    "default": null,
    "constraints": []
   },
   {
    "name": "api_name",
    "type": "string",
    "required": true,
    "description": "Name of the API.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "app_name": "string",
    "api_name": "string",
    "path": "string",
    "method": "string",
    "description": "string",
    "parameters": [
     {
      "name": "string",
      "type": "string",
      "required": true,
      "description": "string",
      "default": null,
      "constraints": [
       "string"
      ]
     }
    ],
    "response_schemas": {
     "success": [
      {}
     ],
     "failure": [
      {}
     ]
    }
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "search_api_docs",
  "path": "/api_docs",
  "method": "GET",
  "description": "Search for relevant API docs.",
  "parameters": [
   {
    "name": "query",
    "type": "string",
    "required": false,
    "description": "The search query string.",
    "default": "",
    "constraints": []
   },
   {
    "name": "page_index",
    "type": "integer",
    "required": false,
    "description": "The index of the page to return.",
    "default": 0,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "page_limit",
    "type": "integer",
    "required": false,
    "description": "The maximum number of results to return per page.",
    "default": 5,
    "constraints": [
     "value >= 1.0, <= 20.0"
    ]
   }
  ],
  "response_schemas": {
   "success": [
    {
     "app_name": "string",
     "api_name": "string",
     "path": "string",
     "method": "string",
     "description": "string",
     "parameters": [
      {
       "name": "string",
       "type": "string",
       "required": true,
       "description": "string",
       "default": null,
       "constraints": [
        "string"
       ]
      }
     ],
     "response_schemas": {
      "success": [
       {}
      ],
      "failure": [
       {}
      ]
     }
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "supervisor",
  "api_name": "show_active_task",
  "path": "/active_task",
  "method": "GET",
  "description": "Show the currently active task assigned to you by the supervisor.",
  "parameters": [],
  "response_schemas": {
   "success": {
    "instruction": "string",
    "status": "string",
    "answer": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 }
]
```


### Environment Interaction 25
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='amazon'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_verification_code",
  "description": "Send account verification code to your email address."
 },
 {
  "name": "verify_account",
  "description": "Verify your account using the verification code sent to your email address."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "show_product",
  "description": "Show product information based on its ID."
 },
 {
  "name": "search_sellers",
  "description": "Search for sellers with a query."
 },
 {
  "name": "show_seller",
  "description": "Show a detailed information about the seller."
 },
 {
  "name": "search_product_types",
  "description": "Search product types present in the database."
 },
 {
  "name": "show_product_feature_choices",
  "description": "Show the choices of colors, relative sizes and sellers aggregated over all products of the given product type. Because it's an aggregation, the choices may not be available for all products. If product type is not passed, it will return the choices for all products in the database."
 },
 {
  "name": "search_products",
  "description": "Search for products with a query and various filtering criteria."
 },
 {
  "name": "show_cart",
  "description": "show your cart."
 },
 {
  "name": "clear_cart",
  "description": "Clear your cart."
 },
 {
  "name": "add_product_to_cart",
  "description": "Add product by id and quantities to your cart."
 },
 {
  "name": "delete_product_from_cart",
  "description": "Remove a product from your cart."
 },
 {
  "name": "update_product_quantity_in_cart",
  "description": "Update product quantity in the user cart."
 },
 {
  "name": "apply_promo_code_to_cart",
  "description": "Apply a promo code to your cart."
 },
 {
  "name": "remove_promo_code_from_cart",
  "description": "Remove a promo code from your cart."
 },
 {
  "name": "show_wish_list",
  "description": "Get list of products in your wishlist."
 },
 {
  "name": "clear_wish_list",
  "description": "Clear wish list."
 },
 {
  "name": "add_product_to_wish_list",
  "description": "Add product by id and quantities to your wish list."
 },
 {
  "name": "delete_product_from_wish_list",
  "description": "Remove product from the user wish list."
 },
 {
  "name": "update_product_quantity_in_wish_list",
  "description": "Update product quantity in the user wish_list."
 },
 {
  "name": "move_product_from_cart_to_wish_list",
  "description": "Move product from the cart to the wish list."
 },
 {
  "name": "move_product_from_wish_list_to_cart",
  "description": "Move product from the wish list to the cart."
 },
 {
  "name": "add_gift_wrapping_to_product",
  "description": "Add gift wrapping to a product in your cart. If the product is already set to be gift wrapped, its quantity will be updated."
 },
 {
  "name": "remove_gift_wrapping_from_product",
  "description": "Remove gift wrapping from a product in your cart."
 },
 {
  "name": "show_orders",
  "description": "Show or search your past orders"
 },
 {
  "name": "place_order",
  "description": "Place an order for all the items in your cart."
 },
 {
  "name": "show_order",
  "description": "Get details of a past order."
 },
 {
  "name": "download_order_receipt",
  "description": "Download the receipt of a past order."
 },
 {
  "name": "show_payment_cards",
  "description": "Get a list of your payment_cards."
 },
 {
  "name": "add_payment_card",
  "description": "Add a new payment card."
 },
 {
  "name": "show_payment_card",
  "description": "Get details of a payment card."
 },
 {
  "name": "delete_payment_card",
  "description": "Delete payment card information."
 },
 {
  "name": "update_payment_card",
  "description": "Update payment card information."
 },
 {
  "name": "show_addresses",
  "description": "Get a list of your addresses."
 },
 {
  "name": "add_address",
  "description": "Add a new address."
 },
 {
  "name": "delete_address",
  "description": "Delete address information."
 },
 {
  "name": "update_address",
  "description": "Update address information."
 },
 {
  "name": "show_product_reviews",
  "description": "Get a list of product reviews."
 },
 {
  "name": "write_product_review",
  "description": "Write a product review."
 },
 {
  "name": "delete_product_review",
  "description": "Delete a product review."
 },
 {
  "name": "update_product_review",
  "description": "Update a product review."
 },
 {
  "name": "show_product_questions",
  "description": "Get a list of product questions."
 },
 {
  "name": "write_product_question",
  "description": "Post a question about a product."
 },
 {
  "name": "show_product_question_answers",
  "description": "Get a list of answers to a product question."
 },
 {
  "name": "write_product_question_answer",
  "description": "Write a answer to a product question."
 },
 {
  "name": "delete_product_question",
  "description": "Delete a product question."
 },
 {
  "name": "update_product_question",
  "description": "Update a product question."
 },
 {
  "name": "delete_product_question_answer",
  "description": "Delete a answer to a product question."
 },
 {
  "name": "update_product_question_answer",
  "description": "Update answer to a product question."
 },
 {
  "name": "show_returns",
  "description": "Get a list of your product returns."
 },
 {
  "name": "initiate_return",
  "description": "Initiate a product return."
 },
 {
  "name": "show_return",
  "description": "Show product return status."
 },
 {
  "name": "show_return_deliverers",
  "description": "Get a list of product return deliverers."
 },
 {
  "name": "show_prime_plans",
  "description": "Show information about prime plans available. Delivery fee is waived for prime members."
 },
 {
  "name": "show_prime_subscriptions",
  "description": "Show your prime subscription history."
 },
 {
  "name": "subscribe_prime",
  "description": "Subscribe to prime membership."
 },
 {
  "name": "download_prime_subscription_receipt",
  "description": "Download the receipt for a prime subscription."
 }
]
```


### Environment Interaction 26
----------------------------------------------------------------------------
```python
print(apis.api_docs.search_api_docs(query='payment_methods', app_name='amazon'))
```

```
[
 {
  "app_name": "api_docs",
  "api_name": "show_app_descriptions",
  "path": "/app_descriptions",
  "method": "GET",
  "description": "Show descriptions for all apps available.",
  "parameters": [],
  "response_schemas": {
   "success": [
    {
     "name": "string",
     "description": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "show_api_descriptions",
  "path": "/api_descriptions",
  "method": "GET",
  "description": "Show descriptions for all APIs available for a given app.",
  "parameters": [
   {
    "name": "app_name",
    "type": "string",
    "required": true,
    "description": "App name to return API descriptions for.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": [
    {
     "name": "string",
     "description": "string"
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "show_api_doc",
  "path": "/api_doc",
  "method": "GET",
  "description": "Show detailed API doc.",
  "parameters": [
   {
    "name": "app_name",
    "type": "string",
    "required": true,
    "description": "App name for the API.",
    "default": null,
    "constraints": []
   },
   {
    "name": "api_name",
    "type": "string",
    "required": true,
    "description": "Name of the API.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "app_name": "string",
    "api_name": "string",
    "path": "string",
    "method": "string",
    "description": "string",
    "parameters": [
     {
      "name": "string",
      "type": "string",
      "required": true,
      "description": "string",
      "default": null,
      "constraints": [
       "string"
      ]
     }
    ],
    "response_schemas": {
     "success": [
      {}
     ],
     "failure": [
      {}
     ]
    }
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "api_docs",
  "api_name": "search_api_docs",
  "path": "/api_docs",
  "method": "GET",
  "description": "Search for relevant API docs.",
  "parameters": [
   {
    "name": "query",
    "type": "string",
    "required": false,
    "description": "The search query string.",
    "default": "",
    "constraints": []
   },
   {
    "name": "page_index",
    "type": "integer",
    "required": false,
    "description": "The index of the page to return.",
    "default": 0,
    "constraints": [
     "value >= 0.0"
    ]
   },
   {
    "name": "page_limit",
    "type": "integer",
    "required": false,
    "description": "The maximum number of results to return per page.",
    "default": 5,
    "constraints": [
     "value >= 1.0, <= 20.0"
    ]
   }
  ],
  "response_schemas": {
   "success": [
    {
     "app_name": "string",
     "api_name": "string",
     "path": "string",
     "method": "string",
     "description": "string",
     "parameters": [
      {
       "name": "string",
       "type": "string",
       "required": true,
       "description": "string",
       "default": null,
       "constraints": [
        "string"
       ]
      }
     ],
     "response_schemas": {
      "success": [
       {}
      ],
      "failure": [
       {}
      ]
     }
    }
   ],
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "supervisor",
  "api_name": "show_active_task",
  "path": "/active_task",
  "method": "GET",
  "description": "Show the currently active task assigned to you by the supervisor.",
  "parameters": [],
  "response_schemas": {
   "success": {
    "instruction": "string",
    "status": "string",
    "answer": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 }
]
```


### Environment Interaction 27
----------------------------------------------------------------------------
```python
print(apis.api_docs.search_api_docs(query='payment', app_name='amazon'))
```

```
[
 {
  "app_name": "splitwise",
  "api_name": "update_payment",
  "path": "/payments/{payment_id}",
  "method": "PATCH",
  "description": "Update payment information.",
  "parameters": [
   {
    "name": "payment_id",
    "type": "integer",
    "required": true,
    "description": "The ID of the payment.",
    "default": null,
    "constraints": []
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from splitwise app login.",
    "default": null,
    "constraints": []
   },
   {
    "name": "amount",
    "type": "number",
    "required": false,
    "description": "The updated amount of the payment.",
    "default": null,
    "constraints": []
   },
   {
    "name": "description",
    "type": "string",
    "required": false,
    "description": "The updated note or description of the payment.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "amazon",
  "api_name": "delete_payment_card",
  "path": "/payment_cards/{payment_card_id}",
  "method": "DELETE",
  "description": "Delete payment card information.",
  "parameters": [
   {
    "name": "payment_card_id",
    "type": "integer",
    "required": true,
    "description": "ID of the payment card to be deleted.",
    "default": null,
    "constraints": []
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "amazon",
  "api_name": "update_payment_card",
  "path": "/payment_cards/{payment_card_id}",
  "method": "PATCH",
  "description": "Update payment card information.",
  "parameters": [
   {
    "name": "payment_card_id",
    "type": "integer",
    "required": true,
    "description": "ID of the payment card to update.",
    "default": null,
    "constraints": []
   },
   {
    "name": "card_name",
    "type": "string",
    "required": true,
    "description": "Name of the payment card to update.",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from amazon app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "delete_payment_card",
  "path": "/payment_cards/{payment_card_id}",
  "method": "DELETE",
  "description": "Delete payment card information.",
  "parameters": [
   {
    "name": "payment_card_id",
    "type": "integer",
    "required": true,
    "description": "ID of the payment card to be deleted.",
    "default": null,
    "constraints": []
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from spotify app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 },
 {
  "app_name": "spotify",
  "api_name": "update_payment_card",
  "path": "/payment_cards/{payment_card_id}",
  "method": "PATCH",
  "description": "Update payment card information.",
  "parameters": [
   {
    "name": "payment_card_id",
    "type": "integer",
    "required": true,
    "description": "ID of the payment card to update.",
    "default": null,
    "constraints": []
   },
   {
    "name": "card_name",
    "type": "string",
    "required": true,
    "description": "Name of the payment card to update.",
    "default": null,
    "constraints": [
     "length >= 1"
    ]
   },
   {
    "name": "access_token",
    "type": "string",
    "required": true,
    "description": "Access token obtained from spotify app login.",
    "default": null,
    "constraints": []
   }
  ],
  "response_schemas": {
   "success": {
    "message": "string"
   },
   "failure": {
    "message": "string"
   }
  }
 }
]
```


### Environment Interaction 28
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='amazon'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_verification_code",
  "description": "Send account verification code to your email address."
 },
 {
  "name": "verify_account",
  "description": "Verify your account using the verification code sent to your email address."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "show_product",
  "description": "Show product information based on its ID."
 },
 {
  "name": "search_sellers",
  "description": "Search for sellers with a query."
 },
 {
  "name": "show_seller",
  "description": "Show a detailed information about the seller."
 },
 {
  "name": "search_product_types",
  "description": "Search product types present in the database."
 },
 {
  "name": "show_product_feature_choices",
  "description": "Show the choices of colors, relative sizes and sellers aggregated over all products of the given product type. Because it's an aggregation, the choices may not be available for all products. If product type is not passed, it will return the choices for all products in the database."
 },
 {
  "name": "search_products",
  "description": "Search for products with a query and various filtering criteria."
 },
 {
  "name": "show_cart",
  "description": "show your cart."
 },
 {
  "name": "clear_cart",
  "description": "Clear your cart."
 },
 {
  "name": "add_product_to_cart",
  "description": "Add product by id and quantities to your cart."
 },
 {
  "name": "delete_product_from_cart",
  "description": "Remove a product from your cart."
 },
 {
  "name": "update_product_quantity_in_cart",
  "description": "Update product quantity in the user cart."
 },
 {
  "name": "apply_promo_code_to_cart",
  "description": "Apply a promo code to your cart."
 },
 {
  "name": "remove_promo_code_from_cart",
  "description": "Remove a promo code from your cart."
 },
 {
  "name": "show_wish_list",
  "description": "Get list of products in your wishlist."
 },
 {
  "name": "clear_wish_list",
  "description": "Clear wish list."
 },
 {
  "name": "add_product_to_wish_list",
  "description": "Add product by id and quantities to your wish list."
 },
 {
  "name": "delete_product_from_wish_list",
  "description": "Remove product from the user wish list."
 },
 {
  "name": "update_product_quantity_in_wish_list",
  "description": "Update product quantity in the user wish_list."
 },
 {
  "name": "move_product_from_cart_to_wish_list",
  "description": "Move product from the cart to the wish list."
 },
 {
  "name": "move_product_from_wish_list_to_cart",
  "description": "Move product from the wish list to the cart."
 },
 {
  "name": "add_gift_wrapping_to_product",
  "description": "Add gift wrapping to a product in your cart. If the product is already set to be gift wrapped, its quantity will be updated."
 },
 {
  "name": "remove_gift_wrapping_from_product",
  "description": "Remove gift wrapping from a product in your cart."
 },
 {
  "name": "show_orders",
  "description": "Show or search your past orders"
 },
 {
  "name": "place_order",
  "description": "Place an order for all the items in your cart."
 },
 {
  "name": "show_order",
  "description": "Get details of a past order."
 },
 {
  "name": "download_order_receipt",
  "description": "Download the receipt of a past order."
 },
 {
  "name": "show_payment_cards",
  "description": "Get a list of your payment_cards."
 },
 {
  "name": "add_payment_card",
  "description": "Add a new payment card."
 },
 {
  "name": "show_payment_card",
  "description": "Get details of a payment card."
 },
 {
  "name": "delete_payment_card",
  "description": "Delete payment card information."
 },
 {
  "name": "update_payment_card",
  "description": "Update payment card information."
 },
 {
  "name": "show_addresses",
  "description": "Get a list of your addresses."
 },
 {
  "name": "add_address",
  "description": "Add a new address."
 },
 {
  "name": "delete_address",
  "description": "Delete address information."
 },
 {
  "name": "update_address",
  "description": "Update address information."
 },
 {
  "name": "show_product_reviews",
  "description": "Get a list of product reviews."
 },
 {
  "name": "write_product_review",
  "description": "Write a product review."
 },
 {
  "name": "delete_product_review",
  "description": "Delete a product review."
 },
 {
  "name": "update_product_review",
  "description": "Update a product review."
 },
 {
  "name": "show_product_questions",
  "description": "Get a list of product questions."
 },
 {
  "name": "write_product_question",
  "description": "Post a question about a product."
 },
 {
  "name": "show_product_question_answers",
  "description": "Get a list of answers to a product question."
 },
 {
  "name": "write_product_question_answer",
  "description": "Write a answer to a product question."
 },
 {
  "name": "delete_product_question",
  "description": "Delete a product question."
 },
 {
  "name": "update_product_question",
  "description": "Update a product question."
 },
 {
  "name": "delete_product_question_answer",
  "description": "Delete a answer to a product question."
 },
 {
  "name": "update_product_question_answer",
  "description": "Update answer to a product question."
 },
 {
  "name": "show_returns",
  "description": "Get a list of your product returns."
 },
 {
  "name": "initiate_return",
  "description": "Initiate a product return."
 },
 {
  "name": "show_return",
  "description": "Show product return status."
 },
 {
  "name": "show_return_deliverers",
  "description": "Get a list of product return deliverers."
 },
 {
  "name": "show_prime_plans",
  "description": "Show information about prime plans available. Delivery fee is waived for prime members."
 },
 {
  "name": "show_prime_subscriptions",
  "description": "Show your prime subscription history."
 },
 {
  "name": "subscribe_prime",
  "description": "Subscribe to prime membership."
 },
 {
  "name": "download_prime_subscription_receipt",
  "description": "Download the receipt for a prime subscription."
 }
]
```


### Environment Interaction 29
----------------------------------------------------------------------------
```python
amazon_password = [p for p in apis.supervisor.show_account_passwords() if p['account_name'] == 'amazon'][0]['password']
access_token = apis.amazon.login(username='chelsea-burch@gmail.com', password=amazon_password)['access_token']
print('Access token:', access_token)
```

```
Access token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbWF6b24rY2hlbHNlYS1idXJjaEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIxNTd9.JP95LdIRrGdZekptTl2D8KTd-YZdUSFHEi__k-RaKDM
```


### Environment Interaction 30
----------------------------------------------------------------------------
```python
addresses = apis.amazon.show_addresses(access_token=access_token)
payment_methods = apis.amazon.show_payment_methods(access_token=access_token)
print('Addresses:', addresses)
print('Payment methods:', payment_methods)
```

```
Execution failed. Traceback:
  File "<python-input>", line 2, in <module>
    payment_methods = apis.amazon.show_payment_methods(access_token=access_token)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: No API named 'show_payment_methods' found in the amazon app.
```


### Environment Interaction 31
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_descriptions(app_name='amazon'))
```

```
[
 {
  "name": "show_account",
  "description": "Show your account information. Unlike show_profile, this includes private information."
 },
 {
  "name": "signup",
  "description": "Sign up to create account."
 },
 {
  "name": "delete_account",
  "description": "Delete your account."
 },
 {
  "name": "update_account_name",
  "description": "Update your first or last name in the account profile."
 },
 {
  "name": "login",
  "description": "Login to your account."
 },
 {
  "name": "logout",
  "description": "Logout from your account."
 },
 {
  "name": "send_verification_code",
  "description": "Send account verification code to your email address."
 },
 {
  "name": "verify_account",
  "description": "Verify your account using the verification code sent to your email address."
 },
 {
  "name": "send_password_reset_code",
  "description": "Send password reset code to your email address."
 },
 {
  "name": "reset_password",
  "description": "Reset your password using the password reset code sent to your email address."
 },
 {
  "name": "show_profile",
  "description": "Show public profile information of a user."
 },
 {
  "name": "show_product",
  "description": "Show product information based on its ID."
 },
 {
  "name": "search_sellers",
  "description": "Search for sellers with a query."
 },
 {
  "name": "show_seller",
  "description": "Show a detailed information about the seller."
 },
 {
  "name": "search_product_types",
  "description": "Search product types present in the database."
 },
 {
  "name": "show_product_feature_choices",
  "description": "Show the choices of colors, relative sizes and sellers aggregated over all products of the given product type. Because it's an aggregation, the choices may not be available for all products. If product type is not passed, it will return the choices for all products in the database."
 },
 {
  "name": "search_products",
  "description": "Search for products with a query and various filtering criteria."
 },
 {
  "name": "show_cart",
  "description": "show your cart."
 },
 {
  "name": "clear_cart",
  "description": "Clear your cart."
 },
 {
  "name": "add_product_to_cart",
  "description": "Add product by id and quantities to your cart."
 },
 {
  "name": "delete_product_from_cart",
  "description": "Remove a product from your cart."
 },
 {
  "name": "update_product_quantity_in_cart",
  "description": "Update product quantity in the user cart."
 },
 {
  "name": "apply_promo_code_to_cart",
  "description": "Apply a promo code to your cart."
 },
 {
  "name": "remove_promo_code_from_cart",
  "description": "Remove a promo code from your cart."
 },
 {
  "name": "show_wish_list",
  "description": "Get list of products in your wishlist."
 },
 {
  "name": "clear_wish_list",
  "description": "Clear wish list."
 },
 {
  "name": "add_product_to_wish_list",
  "description": "Add product by id and quantities to your wish list."
 },
 {
  "name": "delete_product_from_wish_list",
  "description": "Remove product from the user wish list."
 },
 {
  "name": "update_product_quantity_in_wish_list",
  "description": "Update product quantity in the user wish_list."
 },
 {
  "name": "move_product_from_cart_to_wish_list",
  "description": "Move product from the cart to the wish list."
 },
 {
  "name": "move_product_from_wish_list_to_cart",
  "description": "Move product from the wish list to the cart."
 },
 {
  "name": "add_gift_wrapping_to_product",
  "description": "Add gift wrapping to a product in your cart. If the product is already set to be gift wrapped, its quantity will be updated."
 },
 {
  "name": "remove_gift_wrapping_from_product",
  "description": "Remove gift wrapping from a product in your cart."
 },
 {
  "name": "show_orders",
  "description": "Show or search your past orders"
 },
 {
  "name": "place_order",
  "description": "Place an order for all the items in your cart."
 },
 {
  "name": "show_order",
  "description": "Get details of a past order."
 },
 {
  "name": "download_order_receipt",
  "description": "Download the receipt of a past order."
 },
 {
  "name": "show_payment_cards",
  "description": "Get a list of your payment_cards."
 },
 {
  "name": "add_payment_card",
  "description": "Add a new payment card."
 },
 {
  "name": "show_payment_card",
  "description": "Get details of a payment card."
 },
 {
  "name": "delete_payment_card",
  "description": "Delete payment card information."
 },
 {
  "name": "update_payment_card",
  "description": "Update payment card information."
 },
 {
  "name": "show_addresses",
  "description": "Get a list of your addresses."
 },
 {
  "name": "add_address",
  "description": "Add a new address."
 },
 {
  "name": "delete_address",
  "description": "Delete address information."
 },
 {
  "name": "update_address",
  "description": "Update address information."
 },
 {
  "name": "show_product_reviews",
  "description": "Get a list of product reviews."
 },
 {
  "name": "write_product_review",
  "description": "Write a product review."
 },
 {
  "name": "delete_product_review",
  "description": "Delete a product review."
 },
 {
  "name": "update_product_review",
  "description": "Update a product review."
 },
 {
  "name": "show_product_questions",
  "description": "Get a list of product questions."
 },
 {
  "name": "write_product_question",
  "description": "Post a question about a product."
 },
 {
  "name": "show_product_question_answers",
  "description": "Get a list of answers to a product question."
 },
 {
  "name": "write_product_question_answer",
  "description": "Write a answer to a product question."
 },
 {
  "name": "delete_product_question",
  "description": "Delete a product question."
 },
 {
  "name": "update_product_question",
  "description": "Update a product question."
 },
 {
  "name": "delete_product_question_answer",
  "description": "Delete a answer to a product question."
 },
 {
  "name": "update_product_question_answer",
  "description": "Update answer to a product question."
 },
 {
  "name": "show_returns",
  "description": "Get a list of your product returns."
 },
 {
  "name": "initiate_return",
  "description": "Initiate a product return."
 },
 {
  "name": "show_return",
  "description": "Show product return status."
 },
 {
  "name": "show_return_deliverers",
  "description": "Get a list of product return deliverers."
 },
 {
  "name": "show_prime_plans",
  "description": "Show information about prime plans available. Delivery fee is waived for prime members."
 },
 {
  "name": "show_prime_subscriptions",
  "description": "Show your prime subscription history."
 },
 {
  "name": "subscribe_prime",
  "description": "Subscribe to prime membership."
 },
 {
  "name": "download_prime_subscription_receipt",
  "description": "Download the receipt for a prime subscription."
 }
]
```


### Environment Interaction 32
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_order_history'))
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='place_order'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 1, in <module>
    print(apis.api_docs.show_api_doc(app_name='amazon', api_name='show_order_history'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name show_order_history found for the amazon app. Check the api and app name again."}
```


### Environment Interaction 33
----------------------------------------------------------------------------
```python
api_names = [api['name'] for api in apis.api_docs.show_api_descriptions(app_name='amazon')]
print(api_names)
```

```
[
 "show_account",
 "signup",
 "delete_account",
 "update_account_name",
 "login",
 "logout",
 "send_verification_code",
 "verify_account",
 "send_password_reset_code",
 "reset_password",
 "show_profile",
 "show_product",
 "search_sellers",
 "show_seller",
 "search_product_types",
 "show_product_feature_choices",
 "search_products",
 "show_cart",
 "clear_cart",
 "add_product_to_cart",
 "delete_product_from_cart",
 "update_product_quantity_in_cart",
 "apply_promo_code_to_cart",
 "remove_promo_code_from_cart",
 "show_wish_list",
 "clear_wish_list",
 "add_product_to_wish_list",
 "delete_product_from_wish_list",
 "update_product_quantity_in_wish_list",
 "move_product_from_cart_to_wish_list",
 "move_product_from_wish_list_to_cart",
 "add_gift_wrapping_to_product",
 "remove_gift_wrapping_from_product",
 "show_orders",
 "place_order",
 "show_order",
 "download_order_receipt",
 "show_payment_cards",
 "add_payment_card",
 "show_payment_card",
 "delete_payment_card",
 "update_payment_card",
 "show_addresses",
 "add_address",
 "delete_address",
 "update_address",
 "show_product_reviews",
 "write_product_review",
 "delete_product_review",
 "update_product_review",
 "show_product_questions",
 "write_product_question",
 "show_product_question_answers",
 "write_product_question_answer",
 "delete_product_question",
 "update_product_question",
 "delete_product_question_answer",
 "update_product_question_answer",
 "show_returns",
 "initiate_return",
 "show_return",
 "show_return_deliverers",
 "show_prime_plans",
 "show_prime_subscriptions",
 "subscribe_prime",
 "download_prime_subscription_receipt"
]
```


### Environment Interaction 34
----------------------------------------------------------------------------
```python
for name in ['show_orders', 'checkout', 'purchase', 'show_addresses', 'show_payment_methods', 'place_order']:
    try:
        print(name, apis.api_docs.show_api_doc(app_name='amazon', api_name=name))
    except:
        print(name, 'not found')
```

```
show_orders {'app_name': 'amazon', 'api_name': 'show_orders', 'path': '/orders', 'method': 'GET', 'description': 'Show or search your past orders', 'parameters': [{'name': 'access_token', 'type': 'string', 'required': True, 'description': 'Access token obtained from amazon app login.', 'default': None, 'constraints': []}, {'name': 'query', 'type': 'string', 'required': False, 'description': 'Search query string.', 'default': '', 'constraints': []}, {'name': 'page_index', 'type': 'integer', 'required': False, 'description': 'The index of the page to return.', 'default': 0, 'constraints': ['value >= 0.0']}, {'name': 'page_limit', 'type': 'integer', 'required': False, 'description': 'The maximum number of results to return per page.', 'default': 5, 'constraints': ['value >= 1.0, <= 20.0']}, {'name': 'sort_by', 'type': 'string', 'required': False, 'description': 'The attribute to sort the orders by prefixed with +/- to reflect ascending/descending. Valid attributes: created_at. If both query and sort_by are given and non-empty, results will be first ranked by query relevance, then paginated, and will then be sorted by the given attribute within each page. If both query and sort_by are not given, null, or empty, sort_by will default to -created_at.', 'default': None, 'constraints': []}], 'response_schemas': {'success': [{'order_id': 1, 'address_id': 1, 'payment_card_id': 1, 'name': 'string', 'tax': 0.0, 'delivery_fee': 0.0, 'gift_wrap_fee': 0.0, 'discount': 0.0, 'created_at': '2019-01-01T00:00:00', 'address_text': 'string', 'payment_card_digits': 'string', 'paid_amount': 0.0, 'order_items': [{'product_id': 1, 'ordered_quantity': 1, 'returned_quantity': 1, 'gift_wrap_quantity': 1, 'price': 0.0, 'expected_delivery_at': '2019-01-01T00:00:00', 'delivered_at': '2019-01-01T00:00:00'}]}], 'failure': {'message': 'string'}}}
checkout not found
purchase not found
show_addresses {'app_name': 'amazon', 'api_name': 'show_addresses', 'path': '/addresses', 'method': 'GET', 'description': 'Get a list of your addresses.', 'parameters': [{'name': 'access_token', 'type': 'string', 'required': True, 'description': 'Access token obtained from amazon app login.', 'default': None, 'constraints': []}], 'response_schemas': {'success': [{'address_id': 1, 'name': 'string', 'street_address': 'string', 'city': 'string', 'state': 'string', 'country': 'string', 'zip_code': 10000.0}], 'failure': {'message': 'string'}}}
show_payment_methods not found
place_order {'app_name': 'amazon', 'api_name': 'place_order', 'path': '/orders', 'method': 'POST', 'description': 'Place an order for all the items in your cart.', 'parameters': [{'name': 'payment_card_id', 'type': 'integer', 'required': True, 'description': 'ID of the payment card to use for this order.', 'default': None, 'constraints': []}, {'name': 'address_id', 'type': 'integer', 'required': True, 'description': 'ID of the address used for shipping this order.', 'default': None, 'constraints': []}, {'name': 'access_token', 'type': 'string', 'required': True, 'description': 'Access token obtained from amazon app login.', 'default': None, 'constraints': []}], 'response_schemas': {'success': {'message': 'string', 'order_id': 1}, 'failure': {'message': 'string'}}}
```


### Environment Interaction 35
----------------------------------------------------------------------------
```python
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbWF6b24rY2hlbHNlYS1idXJjaEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIxNTd9.JP95LdIRrGdZekptTl2D8KTd-YZdUSFHEi__k-RaKDM'
orders = apis.amazon.show_orders(access_token=access_token, page_limit=20)
print(orders)
```

```
[
 {
  "order_id": 3146,
  "address_id": 69,
  "payment_card_id": 159,
  "name": "1 watch",
  "tax": 10.9,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2023-04-18T12:00:00",
  "address_text": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
  "payment_card_digits": "5067",
  "paid_amount": 119.9,
  "order_items": [
   {
    "product_id": 1406,
    "ordered_quantity": 1,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 109.0,
    "expected_delivery_at": "2023-04-20T18:32:29",
    "delivered_at": "2023-04-20T18:32:29"
   }
  ]
 },
 {
  "order_id": 1029,
  "address_id": 70,
  "payment_card_id": 159,
  "name": "2 cutting boards, 2 snorkel masks, 1 trekking pole",
  "tax": 17.98,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2023-04-13T23:49:07",
  "address_text": "716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529",
  "payment_card_digits": "5067",
  "paid_amount": 197.78,
  "order_items": [
   {
    "product_id": 401,
    "ordered_quantity": 2,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 40.0,
    "expected_delivery_at": "2023-04-19T19:18:01",
    "delivered_at": "2023-04-19T19:18:01"
   },
   {
    "product_id": 1610,
    "ordered_quantity": 2,
    "returned_quantity": 2,
    "gift_wrap_quantity": 0,
    "price": 24.9,
    "expected_delivery_at": "2023-04-15T19:21:53",
    "delivered_at": "2023-04-15T19:21:53"
   },
   {
    "product_id": 2104,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 50.0,
    "expected_delivery_at": "2023-04-16T19:47:13",
    "delivered_at": "2023-04-16T19:47:13"
   }
  ]
 },
 {
  "order_id": 1013,
  "address_id": 69,
  "payment_card_id": 159,
  "name": "2 dumbbells, 2 scissors, 1 kitchen timer, 1 umbrella stand",
  "tax": 117.3,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2023-03-21T01:19:16",
  "address_text": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
  "payment_card_digits": "5067",
  "paid_amount": 1290.3,
  "order_items": [
   {
    "product_id": 1295,
    "ordered_quantity": 2,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 549.0,
    "expected_delivery_at": "2023-03-23T18:04:21",
    "delivered_at": "2023-03-23T18:04:21"
   },
   {
    "product_id": 2213,
    "ordered_quantity": 2,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 7.5,
    "expected_delivery_at": "2023-03-24T18:58:55",
    "delivered_at": "2023-03-24T18:58:55"
   },
   {
    "product_id": 2339,
    "ordered_quantity": 1,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 20.0,
    "expected_delivery_at": "2023-03-23T17:55:16",
    "delivered_at": "2023-03-23T17:55:16"
   },
   {
    "product_id": 2508,
    "ordered_quantity": 1,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 40.0,
    "expected_delivery_at": "2023-03-26T17:10:47",
    "delivered_at": "2023-03-26T17:10:47"
   }
  ]
 },
 {
  "order_id": 1019,
  "address_id": 69,
  "payment_card_id": 158,
  "name": "2 mouse pads",
  "tax": 10.0,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 5.0,
  "discount": 0.0,
  "created_at": "2023-03-13T12:08:43",
  "address_text": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
  "payment_card_digits": "9914",
  "paid_amount": 115.0,
  "order_items": [
   {
    "product_id": 1263,
    "ordered_quantity": 2,
    "returned_quantity": 2,
    "gift_wrap_quantity": 1,
    "price": 50.0,
    "expected_delivery_at": "2023-03-18T18:56:41",
    "delivered_at": "2023-03-18T18:56:41"
   }
  ]
 },
 {
  "order_id": 1018,
  "address_id": 69,
  "payment_card_id": 159,
  "name": "2 sunglasses",
  "tax": 30.8,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2023-02-09T17:03:50",
  "address_text": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
  "payment_card_digits": "5067",
  "paid_amount": 338.8,
  "order_items": [
   {
    "product_id": 1432,
    "ordered_quantity": 2,
    "returned_quantity": 2,
    "gift_wrap_quantity": 0,
    "price": 154.0,
    "expected_delivery_at": "2023-02-15T17:25:45",
    "delivered_at": "2023-02-15T17:25:45"
   }
  ]
 },
 {
  "order_id": 1015,
  "address_id": 69,
  "payment_card_id": 157,
  "name": "1 acoustic guitar, 1 face mask",
  "tax": 331.0,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 5.0,
  "discount": 0.0,
  "created_at": "2023-01-30T19:00:10",
  "address_text": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
  "payment_card_digits": "5688",
  "paid_amount": 3646.0,
  "order_items": [
   {
    "product_id": 1494,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 1,
    "price": 3300.0,
    "expected_delivery_at": "2023-02-04T18:05:38",
    "delivered_at": "2023-02-04T18:05:38"
   },
   {
    "product_id": 2063,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 10.0,
    "expected_delivery_at": "2023-02-01T17:38:59",
    "delivered_at": "2023-02-01T17:38:59"
   }
  ]
 },
 {
  "order_id": 1034,
  "address_id": 70,
  "payment_card_id": 159,
  "name": "1 disinfecting wipe, 1 cookware set, 1 smartphone",
  "tax": 105.5,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2023-01-25T14:41:36",
  "address_text": "716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529",
  "payment_card_digits": "5067",
  "paid_amount": 1160.5,
  "order_items": [
   {
    "product_id": 394,
    "ordered_quantity": 1,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 6.0,
    "expected_delivery_at": "2023-01-29T18:13:13",
    "delivered_at": "2023-01-29T18:13:13"
   },
   {
    "product_id": 529,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 650.0,
    "expected_delivery_at": "2023-02-01T19:37:56",
    "delivered_at": "2023-02-01T19:37:56"
   },
   {
    "product_id": 2410,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 399.0,
    "expected_delivery_at": "2023-01-29T17:36:40",
    "delivered_at": "2023-01-29T17:36:40"
   }
  ]
 },
 {
  "order_id": 1016,
  "address_id": 69,
  "payment_card_id": 159,
  "name": "2 file folders, 1 wireless earbud, 1 hammer, 2 hairbrushes",
  "tax": 36.99,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2023-01-11T12:59:05",
  "address_text": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
  "payment_card_digits": "5067",
  "paid_amount": 406.89,
  "order_items": [
   {
    "product_id": 455,
    "ordered_quantity": 2,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 13.0,
    "expected_delivery_at": "2023-01-16T18:46:13",
    "delivered_at": "2023-01-16T18:46:13"
   },
   {
    "product_id": 733,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 299.9,
    "expected_delivery_at": "2023-01-17T17:51:52",
    "delivered_at": "2023-01-17T17:51:52"
   },
   {
    "product_id": 1348,
    "ordered_quantity": 1,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 20.0,
    "expected_delivery_at": "2023-01-13T19:28:02",
    "delivered_at": "2023-01-13T19:28:02"
   },
   {
    "product_id": 2468,
    "ordered_quantity": 2,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 12.0,
    "expected_delivery_at": "2023-01-15T19:45:37",
    "delivered_at": "2023-01-15T19:45:37"
   }
  ]
 },
 {
  "order_id": 1028,
  "address_id": 70,
  "payment_card_id": 159,
  "name": "1 acoustic guitar, 2 kitchen timers, 1 area rug",
  "tax": 36.3,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 5.0,
  "discount": 0.0,
  "created_at": "2022-12-25T23:36:33",
  "address_text": "716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529",
  "payment_card_digits": "5067",
  "paid_amount": 404.3,
  "order_items": [
   {
    "product_id": 1492,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 1,
    "price": 200.0,
    "expected_delivery_at": "2023-01-01T18:13:02",
    "delivered_at": "2023-01-01T18:13:02"
   },
   {
    "product_id": 2342,
    "ordered_quantity": 2,
    "returned_quantity": 2,
    "gift_wrap_quantity": 0,
    "price": 7.0,
    "expected_delivery_at": "2022-12-26T17:33:19",
    "delivered_at": "2022-12-26T17:33:19"
   },
   {
    "product_id": 2502,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 149.0,
    "expected_delivery_at": "2022-12-28T18:16:16",
    "delivered_at": "2022-12-28T18:16:16"
   }
  ]
 },
 {
  "order_id": 1022,
  "address_id": 69,
  "payment_card_id": 157,
  "name": "1 GPS navigator, 1 ear protection, 1 office chair",
  "tax": 130.4,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2022-12-01T10:36:35",
  "address_text": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
  "payment_card_digits": "5688",
  "paid_amount": 1434.4,
  "order_items": [
   {
    "product_id": 65,
    "ordered_quantity": 1,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 300.0,
    "expected_delivery_at": "2022-12-06T17:08:09",
    "delivered_at": "2022-12-06T17:08:09"
   },
   {
    "product_id": 571,
    "ordered_quantity": 1,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 25.0,
    "expected_delivery_at": "2022-12-03T19:11:07",
    "delivered_at": "2022-12-03T19:11:07"
   },
   {
    "product_id": 633,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 979.0,
    "expected_delivery_at": "2022-12-07T18:45:09",
    "delivered_at": "2022-12-07T18:45:09"
   }
  ]
 },
 {
  "order_id": 1035,
  "address_id": 70,
  "payment_card_id": 159,
  "name": "1 gaming keyboard, 1 telescope, 1 popcorn maker",
  "tax": 63.0,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 5.0,
  "discount": 0.0,
  "created_at": "2022-11-21T19:06:21",
  "address_text": "716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529",
  "payment_card_digits": "5067",
  "paid_amount": 698.0,
  "order_items": [
   {
    "product_id": 436,
    "ordered_quantity": 1,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 200.0,
    "expected_delivery_at": "2022-11-24T17:42:17",
    "delivered_at": "2022-11-24T17:42:17"
   },
   {
    "product_id": 1417,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 1,
    "price": 400.0,
    "expected_delivery_at": "2022-11-28T19:05:18",
    "delivered_at": "2022-11-28T19:05:18"
   },
   {
    "product_id": 2208,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 30.0,
    "expected_delivery_at": "2022-11-25T17:30:13",
    "delivered_at": "2022-11-25T17:30:13"
   }
  ]
 },
 {
  "order_id": 1027,
  "address_id": 70,
  "payment_card_id": 157,
  "name": "2 cookbooks, 1 swimming goggle, 1 baseball cap",
  "tax": 48.5,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2022-11-02T03:27:53",
  "address_text": "716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529",
  "payment_card_digits": "5688",
  "paid_amount": 533.5,
  "order_items": [
   {
    "product_id": 428,
    "ordered_quantity": 2,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 30.0,
    "expected_delivery_at": "2022-11-04T18:24:03",
    "delivered_at": "2022-11-04T18:24:03"
   },
   {
    "product_id": 536,
    "ordered_quantity": 1,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 400.0,
    "expected_delivery_at": "2022-11-04T19:57:09",
    "delivered_at": "2022-11-04T19:57:09"
   },
   {
    "product_id": 2080,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 25.0,
    "expected_delivery_at": "2022-11-06T19:30:40",
    "delivered_at": "2022-11-06T19:30:40"
   }
  ]
 },
 {
  "order_id": 1032,
  "address_id": 70,
  "payment_card_id": 158,
  "name": "1 corkboard, 2 winter coats, 1 compass",
  "tax": 39.3,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2022-10-17T14:31:18",
  "address_text": "716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529",
  "payment_card_digits": "9914",
  "paid_amount": 432.3,
  "order_items": [
   {
    "product_id": 562,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 13.0,
    "expected_delivery_at": "2022-10-18T17:17:29",
    "delivered_at": "2022-10-18T17:17:29"
   },
   {
    "product_id": 2245,
    "ordered_quantity": 2,
    "returned_quantity": 2,
    "gift_wrap_quantity": 0,
    "price": 160.0,
    "expected_delivery_at": "2022-10-20T19:00:00",
    "delivered_at": "2022-10-20T19:00:00"
   },
   {
    "product_id": 2457,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 60.0,
    "expected_delivery_at": "2022-10-18T17:35:32",
    "delivered_at": "2022-10-18T17:35:32"
   }
  ]
 },
 {
  "order_id": 1021,
  "address_id": 69,
  "payment_card_id": 157,
  "name": "2 water bottles, 1 cooling fan",
  "tax": 5.58,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2022-10-15T11:32:15",
  "address_text": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
  "payment_card_digits": "5688",
  "paid_amount": 61.38,
  "order_items": [
   {
    "product_id": 361,
    "ordered_quantity": 2,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 19.9,
    "expected_delivery_at": "2022-10-18T17:34:35",
    "delivered_at": "2022-10-18T17:34:35"
   },
   {
    "product_id": 2119,
    "ordered_quantity": 1,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 16.0,
    "expected_delivery_at": "2022-10-17T18:35:43",
    "delivered_at": "2022-10-17T18:35:43"
   }
  ]
 },
 {
  "order_id": 1014,
  "address_id": 69,
  "payment_card_id": 157,
  "name": "2 golf clubs, 2 fire extinguishers",
  "tax": 170.0,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2022-10-11T12:06:17",
  "address_text": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
  "payment_card_digits": "5688",
  "paid_amount": 1870.0,
  "order_items": [
   {
    "product_id": 2589,
    "ordered_quantity": 2,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 800.0,
    "expected_delivery_at": "2022-10-12T19:55:34",
    "delivered_at": "2022-10-12T19:55:34"
   },
   {
    "product_id": 2655,
    "ordered_quantity": 2,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 50.0,
    "expected_delivery_at": "2022-10-15T17:25:23",
    "delivered_at": "2022-10-15T17:25:23"
   }
  ]
 },
 {
  "order_id": 1020,
  "address_id": 69,
  "payment_card_id": 158,
  "name": "2 cooling fans, 2 umbrella stands",
  "tax": 31.0,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2022-09-25T14:12:36",
  "address_text": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
  "payment_card_digits": "9914",
  "paid_amount": 341.0,
  "order_items": [
   {
    "product_id": 2120,
    "ordered_quantity": 2,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 65.0,
    "expected_delivery_at": "2022-10-02T17:46:48",
    "delivered_at": "2022-10-02T17:46:48"
   },
   {
    "product_id": 2511,
    "ordered_quantity": 2,
    "returned_quantity": 2,
    "gift_wrap_quantity": 0,
    "price": 90.0,
    "expected_delivery_at": "2022-09-29T17:52:56",
    "delivered_at": "2022-09-29T17:52:56"
   }
  ]
 },
 {
  "order_id": 1026,
  "address_id": 70,
  "payment_card_id": 159,
  "name": "1 bath towel, 2 lawn mowers, 2 ski poles, 2 picture frames",
  "tax": 84.4,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2022-09-15T18:05:18",
  "address_text": "716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529",
  "payment_card_digits": "5067",
  "paid_amount": 928.4,
  "order_items": [
   {
    "product_id": 559,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 20.0,
    "expected_delivery_at": "2022-09-16T18:00:44",
    "delivered_at": "2022-09-16T18:00:44"
   },
   {
    "product_id": 1205,
    "ordered_quantity": 2,
    "returned_quantity": 2,
    "gift_wrap_quantity": 0,
    "price": 349.0,
    "expected_delivery_at": "2022-09-22T19:46:47",
    "delivered_at": "2022-09-22T19:46:47"
   },
   {
    "product_id": 1498,
    "ordered_quantity": 2,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 50.0,
    "expected_delivery_at": "2022-09-18T19:00:34",
    "delivered_at": "2022-09-18T19:00:34"
   },
   {
    "product_id": 1529,
    "ordered_quantity": 2,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 13.0,
    "expected_delivery_at": "2022-09-18T19:40:35",
    "delivered_at": "2022-09-18T19:40:35"
   }
  ]
 },
 {
  "order_id": 1017,
  "address_id": 69,
  "payment_card_id": 159,
  "name": "1 flute, 1 electric shaver, 2 medicine balls",
  "tax": 155.3,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2022-08-31T17:34:08",
  "address_text": "46567 Matthew Burg Suite 702\nSeattle\nWashington\nUnited States\n15473",
  "payment_card_digits": "5067",
  "paid_amount": 1708.3,
  "order_items": [
   {
    "product_id": 18,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 1300.0,
    "expected_delivery_at": "2022-09-03T19:56:44",
    "delivered_at": "2022-09-03T19:56:44"
   },
   {
    "product_id": 2300,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 80.0,
    "expected_delivery_at": "2022-09-04T19:40:29",
    "delivered_at": "2022-09-04T19:40:29"
   },
   {
    "product_id": 2408,
    "ordered_quantity": 2,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 86.5,
    "expected_delivery_at": "2022-09-02T17:19:55",
    "delivered_at": "2022-09-02T17:19:55"
   }
  ]
 },
 {
  "order_id": 1033,
  "address_id": 70,
  "payment_card_id": 157,
  "name": "2 harps, 1 smart thermostat, 1 picture frame",
  "tax": 720.9,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2022-08-26T03:25:45",
  "address_text": "716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529",
  "payment_card_digits": "5688",
  "paid_amount": 7929.9,
  "order_items": [
   {
    "product_id": 457,
    "ordered_quantity": 2,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 3495.0,
    "expected_delivery_at": "2022-08-30T19:30:12",
    "delivered_at": "2022-08-30T19:30:12"
   },
   {
    "product_id": 1462,
    "ordered_quantity": 1,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 189.0,
    "expected_delivery_at": "2022-08-30T18:19:57",
    "delivered_at": "2022-08-30T18:19:57"
   },
   {
    "product_id": 1535,
    "ordered_quantity": 1,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 30.0,
    "expected_delivery_at": "2022-09-01T17:12:03",
    "delivered_at": "2022-09-01T17:12:03"
   }
  ]
 },
 {
  "order_id": 1023,
  "address_id": 70,
  "payment_card_id": 157,
  "name": "2 beach chairs, 2 coffee makers",
  "tax": 37.96,
  "delivery_fee": 0.0,
  "gift_wrap_fee": 0.0,
  "discount": 0.0,
  "created_at": "2022-08-22T03:39:08",
  "address_text": "716 White Drive Suite 52\nSeattle\nWashington\nUnited States\n47529",
  "payment_card_digits": "5688",
  "paid_amount": 417.56,
  "order_items": [
   {
    "product_id": 1338,
    "ordered_quantity": 2,
    "returned_quantity": 0,
    "gift_wrap_quantity": 0,
    "price": 40.8,
    "expected_delivery_at": "2022-08-29T19:06:38",
    "delivered_at": "2022-08-29T19:06:38"
   },
   {
    "product_id": 1391,
    "ordered_quantity": 2,
    "returned_quantity": 1,
    "gift_wrap_quantity": 0,
    "price": 149.0,
    "expected_delivery_at": "2022-08-29T19:45:03",
    "delivered_at": "2022-08-29T19:45:03"
   }
  ]
 }
]
```


### Environment Interaction 36
----------------------------------------------------------------------------
```python
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbWF6b24rY2hlbHNlYS1idXJjaEBnbWFpbC5jb20iLCJleHAiOjE2ODQ0MTIxNTd9.JP95LdIRrGdZekptTl2D8KTd-YZdUSFHEi__k-RaKDM'
product_info = apis.amazon.show_product(access_token=access_token, product_id=1406)
print(product_info)
```

```
{
 "product_id": 1406,
 "seller_id": 184,
 "product_type": "watch",
 "name": "Fossil Men's The Minimalist Quartz Watch",
 "description": "Simple and stylish quartz watch for men",
 "price": 109.0,
 "delivery_days": 2,
 "inventory_quantity": 5,
 "weight": 0.2,
 "length": 2.0,
 "width": 2.0,
 "height": 0.4,
 "color": "brown",
 "relative_size": "medium",
 "rating": 3.8,
 "num_product_reviews": 6,
 "num_product_questions": 4,
 "variations": []
}
```


### Environment Interaction 37
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='add_to_cart'))
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='checkout'))
```

```
Execution failed. Traceback:
  File "<python-input>", line 1, in <module>
    print(apis.api_docs.show_api_doc(app_name='amazon', api_name='add_to_cart'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Exception: Response status code is 422:
{"message":"No APIs with name add_to_cart found for the amazon app. Check the api and app name again."}
```


### Environment Interaction 38
----------------------------------------------------------------------------
```python
all_apis = apis.api_docs.show_api_descriptions(app_name='amazon')
[print(a['name']) for a in all_apis]
```

```
show_account
signup
delete_account
update_account_name
login
logout
send_verification_code
verify_account
send_password_reset_code
reset_password
show_profile
show_product
search_sellers
show_seller
search_product_types
show_product_feature_choices
search_products
show_cart
clear_cart
add_product_to_cart
delete_product_from_cart
update_product_quantity_in_cart
apply_promo_code_to_cart
remove_promo_code_from_cart
show_wish_list
clear_wish_list
add_product_to_wish_list
delete_product_from_wish_list
update_product_quantity_in_wish_list
move_product_from_cart_to_wish_list
move_product_from_wish_list_to_cart
add_gift_wrapping_to_product
remove_gift_wrapping_from_product
show_orders
place_order
show_order
download_order_receipt
show_payment_cards
add_payment_card
show_payment_card
delete_payment_card
update_payment_card
show_addresses
add_address
delete_address
update_address
show_product_reviews
write_product_review
delete_product_review
update_product_review
show_product_questions
write_product_question
show_product_question_answers
write_product_question_answer
delete_product_question
update_product_question
delete_product_question_answer
update_product_question_answer
show_returns
initiate_return
show_return
show_return_deliverers
show_prime_plans
show_prime_subscriptions
subscribe_prime
download_prime_subscription_receipt
```


### Environment Interaction 39
----------------------------------------------------------------------------
```python
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='add_product_to_cart'))
print(apis.api_docs.show_api_doc(app_name='amazon', api_name='place_order'))
```

```
{
 "app_name": "amazon",
 "api_name": "add_product_to_cart",
 "path": "/cart/{product_id}",
 "method": "POST",
 "description": "Add product by id and quantities to your cart.",
 "parameters": [
  {
   "name": "product_id",
   "type": "integer",
   "required": true,
   "description": "ID of the product to be added to the cart.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from amazon app login.",
   "default": null,
   "constraints": []
  },
  {
   "name": "quantity",
   "type": "integer",
   "required": false,
   "description": "The quantity of the product to be added to the cart.",
   "default": 1,
   "constraints": [
    "value >= 1.0"
   ]
  },
  {
   "name": "clear_cart_first",
   "type": "boolean",
   "required": false,
   "description": "If true, the cart will be cleared before adding the product to the cart.",
   "default": false,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string"
  },
  "failure": {
   "message": "string"
  }
 }
}
{
 "app_name": "amazon",
 "api_name": "place_order",
 "path": "/orders",
 "method": "POST",
 "description": "Place an order for all the items in your cart.",
 "parameters": [
  {
   "name": "payment_card_id",
   "type": "integer",
   "required": true,
   "description": "ID of the payment card to use for this order.",
   "default": null,
   "constraints": []
  },
  {
   "name": "address_id",
   "type": "integer",
   "required": true,
   "description": "ID of the address used for shipping this order.",
   "default": null,
   "constraints": []
  },
  {
   "name": "access_token",
   "type": "string",
   "required": true,
   "description": "Access token obtained from amazon app login.",
   "default": null,
   "constraints": []
  }
 ],
 "response_schemas": {
  "success": {
   "message": "string",
   "order_id": 1
  },
  "failure": {
   "message": "string"
  }
 }
}
```


### Environment Interaction 40
----------------------------------------------------------------------------
```python
for a in apis.api_docs.show_api_descriptions(app_name='amazon'):
    print(a['name'])
```

```
show_account
signup
delete_account
update_account_name
login
logout
send_verification_code
verify_account
send_password_reset_code
reset_password
show_profile
show_product
search_sellers
show_seller
search_product_types
show_product_feature_choices
search_products
show_cart
clear_cart
add_product_to_cart
delete_product_from_cart
update_product_quantity_in_cart
apply_promo_code_to_cart
remove_promo_code_from_cart
show_wish_list
clear_wish_list
add_product_to_wish_list
delete_product_from_wish_list
update_product_quantity_in_wish_list
move_product_from_cart_to_wish_list
move_product_from_wish_list_to_cart
add_gift_wrapping_to_product
remove_gift_wrapping_from_product
show_orders
place_order
show_order
download_order_receipt
show_payment_cards
add_payment_card
show_payment_card
delete_payment_card
update_payment_card
show_addresses
add_address
delete_address
update_address
show_product_reviews
write_product_review
delete_product_review
update_product_review
show_product_questions
write_product_question
show_product_question_answers
write_product_question_answer
delete_product_question
update_product_question
delete_product_question_answer
update_product_question_answer
show_returns
initiate_return
show_return
show_return_deliverers
show_prime_plans
show_prime_subscriptions
subscribe_prime
download_prime_subscription_receipt
```

