
public class OtherIncome implements Income {
	protected double income;
	
	public OtherIncome (double income) {
		this.income = income;
	}
	
	@Override
	public double getTax() {
	
		return income * 0.1;
	}

}
