function timeInWords(h, m) {
    let hours = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'quarter', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 21:'twenty one', 22:'twenty two', 23:'twenty three', 24:'twenty four', 25:'twenty five', 26:'twenty six', 27:'twenty seven', 28:'twenty eight', 29:'twenty nine', 30:'half'}
  
    let oclock = "o' clock"
    let past = "past"
    let to = "to"
    let half = "half"
    if(m === 30){
      return `${half} ${past} ${hours[h]}`
    }
    else if(m === 0){
      return `${hours[h]} ${oclock}`
    }
    else if(m === 1){
      return `${hours[m]} minute ${past} ${hours[h]}`
    }
    else if(m === 15){
      return `${hours[m]} ${past} ${hours[h]}`
    }
    else if(m > 0 && m < 15 || m > 15 && m < 30){
      return `${hours[m]} minutes ${past} ${hours[h]}`
    } 
    else if(m === 45){
      let newm = 60-m
      return `${hours[newm]} to ${hours[h+1]}`
    }
    else if(m > 30 && m < 45 || m > 45 && m < 60){
      let newm = 60-m
      return `${hours[newm]} minutes to ${hours[h+1]}`
    }
    
  
  }
  console.log(timeInWords(5,46))