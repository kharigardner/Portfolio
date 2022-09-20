/* This script is a simple banking application that allows a user to create an account, deposit money, withdraw money, and check their balance. */

class Account(id:String, n:Int, b:Double) {
    val nic:String = id
    val acnumber: Int = n
    var balance: Double = b

    override def toString = "["+nic+":"+acnumber +":"+ balance+"]"
}

class AccountList {
    var list:List[Account] = List()

    def addAccount(a:Account) = list = list ::: List(a)

    def removeAccount(n:String) = list = list.filter(x => x.nic != n)

    def findAccount(n:String):Account = list.filter(x => x.nic == n)(0)

    def totalBalance = list.reduce((x,y) => new Account("",0,x.balance+y.balance)).balance

    def interest = list.map(x => if(x.balance >= 0) x.balance*0.05 else x.balance*0.1)

    def printAccounts = list.foreach(x => println(x))
}

class Bank {
    var accountList = new AccountList()

    def openAccount(nic:String, acnumber:Int, balance:Double) = accountList.addAccount(new Account(nic, acnumber, balance))

    def closeAccount(nic:String) = accountList.removeAccount(nic)

    def findAccount(nic:String) = accountList.findAccount(nic)

    def totalBalance = accountList.totalBalance

    def interest = accountList.interest

    def printAccounts = accountList.printAccounts
}

class Customer(id:String, n:Int, b:Double) extends Account(id, n, b) {
    override def toString = "["+nic+":"+acnumber +":"+ balance+"]"
}

class CustomerList {
    var list:List[Customer] = List()

    def addCustomer(a:Customer) = list = list ::: List(a)

    def removeCustomer(n:String) = list = list.filter(x => x.nic != n)

    def findCustomer(n:String):Customer = list.filter(x => x.nic == n)(0)

    def totalBalance = list.reduce((x,y) => new Customer("",0,x.balance+y.balance)).balance

    def interest = list.map(x => if(x.balance >= 0) x.balance*0.05 else x.balance*0.1)

    def printCustomers = list.foreach(x => println(x))
}

/* now we create a inmemory database for the bank */
import scala.collection.mutable.Map

// create a map to store the bank information using the classes defined above
val bank:Map[String, Bank] = Map()

// create a function to add a bank to the map
def addBank(name:String, b:Bank) = bank += (name -> b)

// create a function to find a bank from the map
def findBank(name:String):Bank = bank(name)

// create a function to list all banks in the map
def listBanks = bank.keys.foreach(x => println(x))

// create a function to remove a bank from the map
def removeBank(name:String) = bank -= name

// use the class methods to create a bank, account, and customer
val bank1 = new Bank
bank1.openAccount("1", 1, 1000)
bank1.openAccount("2", 2, 2000)
bank1.openAccount("3", 3, 3000)
bank1.openAccount("4", 4, 4000)

val account1 = bank1.findAccount("1")
val customer1 = new Customer("1", 1, 1000)
val customerList1 = new CustomerList