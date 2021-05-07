namespace DemoGame.domain.units
{
	public class Knight : IUnit
	{
		public int Id => 3;
		public string Name => "Knight";
		public int HitPoints => 30;
		public int Attack => 30;
		public int Defence => 30;
		public int Cost => 30;
		public bool Cloneable => false;
		public bool Curable => true;

		public double SpecialActionProbability => 0.5;
		public void SpecialAction(Army friends, Army enemies)
		{
			throw new System.NotImplementedException();
		}
	}
}