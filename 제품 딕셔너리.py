product={'비누','칫솔','샴푸','치약','로션'}
sale={'칫솔','치약','로션'}
customer={'칫솔','치약'}
good = sale and customer
bad = product - (sale or customer)
      
