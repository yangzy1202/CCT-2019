
public class RoyaltyIncome implements Income {
	protected double income;
	
	public RoyaltyIncome(double income) {
		this.income = income;
	}
	
	@Override
	public double getTax() {
		return income * 0.2;
	}

}
