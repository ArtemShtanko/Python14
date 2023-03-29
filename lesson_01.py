
message = "Hello World!"
message_changed_invert = message [::-1] # message_invert ## !dlroW olleH
message_changed_delete = message [::2] # delete each 2 symbol from the begin ## HloWrd
message_changed_delete_invert = message [::-2] # delete each 2 symbol from the end ## !lo le

print (message, "->", message_changed_invert, "->", message_changed_delete, "->", message_changed_delete_invert) # Hello World! -> !dlroW olleH -> !lo le




