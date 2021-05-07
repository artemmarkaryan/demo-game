namespace DemoGame.domain.units
{
	public class Wizard : IUnit
	{
		public int Id => 4;
		public string Name => "Wizard";
		public int HitPoints => 20;
		public int Attack => 20;
		public int Defence => 10;
		public int Cost => 30;
		public bool Cloneable => false;
		public bool Curable => false;

		public double SpecialActionProbability => 0.5;
		public void SpecialAction(Army friends, Army enemies)
		{
			throw new System.NotImplementedException();
		}
	}
}