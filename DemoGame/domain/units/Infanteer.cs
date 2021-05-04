namespace DemoGame.domain.units {
public class Infanteer : IUnit {
	public int Id => 0;
	public string Name => "Infanteer";
	public int HitPoints => 20;
	public int Attack => 10;
	public int Defence => 10;
	public int Cost => 10;
	public bool Cloneable => true;

	public double SpecialActionProbability => 0.5;
	public void SpecialAction(Army friends, Army enemies) {
		throw new System.NotImplementedException();
	}
}
}