namespace DemoGame.domain.units
{
	public class Archer : IUnit
	{
		public int Id => 0;
		public string Name => "Archer";
		public int HitPoints => 20;
		public int Attack => 10;
		public int Defence => 10;
		public int Cost => 20;
		public bool Cloneable => true;
		public bool Curable => true;

		public double SpecialActionProbability => 0.5;
		public void SpecialAction(Army friends, Army enemies)
		{
			throw new System.NotImplementedException();
		}
	}
}